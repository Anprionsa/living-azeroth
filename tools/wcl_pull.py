#!/usr/bin/env python3
"""Warcraft Logs control puller for the Classic+ project.

Implements tier one of files/absolute-numbers.md: primary-sourced Season of
Mastery and Anniversary Naxxramas ladders, pulled through the v2 GraphQL API,
with partition, percentile, encounter, window and sample size on every number.

Credentials come from the environment (WCL_CLIENT_ID, WCL_CLIENT_SECRET) or
from files/wcl.env, never from arguments, and are never printed.

Modes
  --dry-run       print the plan and the query shapes; no network; then drives
                  discovery, pull, resume, reduce and render against an
                  in-memory stand-in for the API, under files/controls/dry-run/
  --token-check   obtain a token and read rateLimitData on each host
  --discover      run discovery only and write files/controls/wcl-ids.json
  (default)       discover, pull, reduce, write controls.json and controls.md
  --resume        reuse wcl-ids.json and skip cells recorded complete
  --reduce-only   rebuild controls.json and controls.md from the raw cache

Standard library only, with requests used when it is installed.
"""
from __future__ import annotations

import argparse
import base64
import datetime as _dt
import hashlib
import json
import os
import random
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

try:  # optional
    import requests as _requests  # type: ignore
except Exception:  # pragma: no cover
    _requests = None

import urllib.error
import urllib.request

VERSION = "0.1"
USER_AGENT = f"living-azeroth-wcl-pull/{VERSION}"
TOKEN_URL = "https://www.warcraftlogs.com/oauth/token"

# ---------------------------------------------------------------------------
# Plan constants. Everything under MEMO_* is what absolute-numbers.md says and
# is verified against worldData at runtime; nothing here is trusted blindly.
# ---------------------------------------------------------------------------

SOURCES = {
    "som": {
        "label": "Season of Mastery",
        "host": "vanilla.warcraftlogs.com",
        "memoZoneId": 2006,
        "partitionMatch": r"season of mastery|\bsom\b",
        "partitionRule": "partition whose name matches 'Season of Mastery'",
        "worldBuffs": False,
        "note": "primary control; matches classic-plus on world buffs, debuff limit and batching",
    },
    "anniversary": {
        "label": "Anniversary",
        "host": "fresh.warcraftlogs.com",
        "memoZoneId": 1036,
        "partitionMatch": None,
        "partitionRule": "the zone's default partition, else the highest partition id",
        "worldBuffs": True,
        "note": "secondary control; world buffs present via Chronoboon",
    },
}

# key -> (name matcher, expected name, scenario, role in the reading)
ENCOUNTERS = {
    "patchwerk": (r"patchwerk", "Patchwerk", "patchwerk", "primary"),
    "heigan": (r"heigan", "Heigan the Unclean", "movement", "primary"),
    "faerlina": (r"faerlina", "Grand Widow Faerlina", "cleave", "primary"),
    "gothik": (r"gothik", "Gothik the Harvester", "switching", "primary"),
    "loatheb": (r"loatheb", "Loatheb", "patchwerk", "check"),
    "sapphiron": (r"sapphiron", "Sapphiron", "movement", "check"),
    "horsemen": (r"horsemen", "The Four Horsemen", "switching", "check"),
}
# encounters where bossdps is also pulled so add damage can be isolated
CLEAVE_ENCOUNTERS = ("faerlina", "gothik")

# specKey -> (className, specName, group)
SPECS = {
    "warrior-arms": ("Warrior", "Arms", "dps"),
    "warrior-fury": ("Warrior", "Fury", "dps"),
    "rogue-combat": ("Rogue", "Combat", "dps"),
    "mage-fire": ("Mage", "Fire", "dps"),
    "mage-frost": ("Mage", "Frost", "dps"),
    "warlock-affliction": ("Warlock", "Affliction", "dps"),
    "warlock-destruction": ("Warlock", "Destruction", "dps"),
    "hunter-marksmanship": ("Hunter", "Marksmanship", "dps"),
    "druid-feral": ("Druid", "Feral", "dps"),
    "druid-balance": ("Druid", "Balance", "dps"),
    "shaman-enhancement": ("Shaman", "Enhancement", "dps"),
    "shaman-elemental": ("Shaman", "Elemental", "dps"),
    "priest-shadow": ("Priest", "Shadow", "dps"),
    "paladin-retribution": ("Paladin", "Retribution", "dps"),
    # thin on SoM per the memo; pulled and reported as thin, not dropped
    "hunter-survival": ("Hunter", "Survival", "thin"),
    "rogue-subtlety": ("Rogue", "Subtlety", "thin"),
    "mage-arcane": ("Mage", "Arcane", "thin"),
    # healers
    "priest-holy": ("Priest", "Holy", "healer"),
    "priest-discipline": ("Priest", "Discipline", "healer"),
    "druid-restoration": ("Druid", "Restoration", "healer"),
    "shaman-restoration": ("Shaman", "Restoration", "healer"),
    "paladin-holy": ("Paladin", "Holy", "healer"),
}

PERCENTILES = (50, 75, 95)
THIN_SAMPLE = 30  # below this the cell is reported as thin
DEFAULT_WINDOW_DAYS = 56
DEFAULT_COST_ESTIMATE = 10.0  # points per rankings page, memo's pessimistic budget

# ---------------------------------------------------------------------------
# GraphQL documents
# ---------------------------------------------------------------------------

Q_RATE = """query RateLimit {
  rateLimitData { limitPerHour pointsSpentThisHour pointsResetIn }
}"""

Q_DISCOVERY = """query Discovery {
  rateLimitData { limitPerHour pointsSpentThisHour pointsResetIn }
  worldData {
    zones {
      id
      name
      frozen
      expansion { id name }
      partitions { id name compactName default }
      encounters { id name }
    }
  }
  gameData {
    classes { id name slug specs { id name slug } }
    factions { id name }
  }
}"""

Q_RANKINGS = """query Rankings($encounter: Int!, $className: String!, $specName: String!, $metric: CharacterRankingMetricType!, $partition: Int!, $page: Int!, $combatant: Boolean!) {
  rateLimitData { limitPerHour pointsSpentThisHour pointsResetIn }
  worldData {
    encounter(id: $encounter) {
      id
      name
      characterRankings(className: $className, specName: $specName, metric: $metric, partition: $partition, page: $page, includeCombatantInfo: $combatant)
    }
  }
}"""


def qhash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


# ---------------------------------------------------------------------------
# Small utilities
# ---------------------------------------------------------------------------

def now_iso() -> str:
    return _dt.datetime.now(_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def ms_to_iso(ms) -> str | None:
    if ms is None:
        return None
    try:
        return _dt.datetime.fromtimestamp(ms / 1000.0, tz=_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    except Exception:
        return None


def parse_date(text: str) -> _dt.datetime:
    return _dt.datetime.strptime(text, "%Y-%m-%d").replace(tzinfo=_dt.timezone.utc)


def write_json_atomic(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=1, ensure_ascii=True, sort_keys=False)
        fh.write("\n")
    os.replace(tmp, path)


def read_json(path: Path, default=None):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        return default


def fmt_int(n) -> str:
    if n is None:
        return "-"
    return f"{int(round(n)):,}"


def nearest_rank(sorted_vals: list, p: int):
    """Nearest-rank percentile on an ascending list. Returns (value, rank) or (None, None)."""
    n = len(sorted_vals)
    if n == 0:
        return None, None
    import math
    k = max(1, min(n, math.ceil(p / 100.0 * n)))
    return sorted_vals[k - 1], k


class Log:
    def __init__(self, path: Path | None):
        self.path = path
        if path is not None:
            path.parent.mkdir(parents=True, exist_ok=True)

    def __call__(self, msg: str = "") -> None:
        line = msg
        try:
            print(line, flush=True)
        except UnicodeEncodeError:
            print(line.encode("ascii", "replace").decode("ascii"), flush=True)
        if self.path is not None:
            with open(self.path, "a", encoding="utf-8") as fh:
                fh.write(f"{now_iso()} {line}\n")


# ---------------------------------------------------------------------------
# Credentials
# ---------------------------------------------------------------------------

def parse_env_file(path: Path) -> dict:
    out = {}
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return out
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[len("export "):].strip()
        if "=" not in line:
            continue
        key, val = line.split("=", 1)
        key = key.strip()
        val = val.strip()
        if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
            val = val[1:-1]
        out[key] = val
    return out


def load_credentials(root: Path) -> tuple[str | None, str | None, str]:
    """Returns (client_id, client_secret, origin). Values are never logged."""
    cid = os.environ.get("WCL_CLIENT_ID")
    sec = os.environ.get("WCL_CLIENT_SECRET")
    if cid and sec:
        return cid, sec, "environment"
    env_path = root / "files" / "wcl.env"
    filed = parse_env_file(env_path)
    cid = cid or filed.get("WCL_CLIENT_ID")
    sec = sec or filed.get("WCL_CLIENT_SECRET")
    if cid and sec:
        origin = "files/wcl.env" if not (os.environ.get("WCL_CLIENT_ID") or os.environ.get("WCL_CLIENT_SECRET")) else "environment and files/wcl.env"
        return cid, sec, origin
    return None, None, "none"


def gitignore_status(root: Path, rel: str) -> str:
    """Says whether git ignores rel, without failing when git is absent."""
    try:
        r = subprocess.run(["git", "check-ignore", "-q", rel], cwd=str(root),
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=10)
        if r.returncode == 0:
            return "ignored"
        if r.returncode == 1:
            return "NOT ignored"
        return "unknown"
    except Exception:
        return "unknown (git not available)"


# ---------------------------------------------------------------------------
# HTTP layer: requests when present, urllib otherwise
# ---------------------------------------------------------------------------

class HttpResponse:
    def __init__(self, status: int, headers: dict, text: str):
        self.status = status
        self.headers = {k.lower(): v for k, v in headers.items()}
        self.text = text

    def json(self):
        return json.loads(self.text) if self.text else None


def http_post(url: str, headers: dict, body: bytes, timeout: float = 60.0) -> HttpResponse:
    if _requests is not None:
        r = _requests.post(url, headers=headers, data=body, timeout=timeout)
        return HttpResponse(r.status_code, dict(r.headers), r.text)
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return HttpResponse(resp.status, dict(resp.headers.items()), resp.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as e:
        try:
            text = e.read().decode("utf-8", "replace")
        except Exception:
            text = ""
        return HttpResponse(e.code, dict(e.headers.items()) if e.headers else {}, text)


class TransientError(Exception):
    pass


class RateLimited(Exception):
    def __init__(self, wait: float, msg: str = "rate limited"):
        super().__init__(msg)
        self.wait = wait


class FatalError(Exception):
    pass


# ---------------------------------------------------------------------------
# Rate limiter
# ---------------------------------------------------------------------------

class RateLimiter:
    """Tracks rateLimitData and decides when to wait.

    The point cost of a rankings page is undocumented; it is measured from the
    delta of pointsSpentThisHour between consecutive responses on the same host
    and smoothed. Until a measurement exists the memo's ten points is assumed.
    """

    def __init__(self, margin_points: float = 0.0, cost_estimate: float = DEFAULT_COST_ESTIMATE, sleep=time.sleep, log=print):
        self.limit = None
        self.spent = None
        self.reset_in = None
        self.updated = None
        self.margin = margin_points
        self.cost = cost_estimate
        self.measured = 0
        self.sleep = sleep
        self.log = log

    def update(self, data: dict | None, measure: bool = False) -> None:
        """Records the latest rateLimitData; measures per-page cost only when asked (rankings pages)."""
        if not data:
            return
        limit = data.get("limitPerHour")
        spent = data.get("pointsSpentThisHour")
        reset = data.get("pointsResetIn")
        if measure and self.spent is not None and spent is not None and spent > self.spent:
            delta = spent - self.spent
            if 0 < delta < 500:
                self.cost = delta if self.measured == 0 else 0.7 * self.cost + 0.3 * delta
                self.measured += 1
        self.limit, self.spent, self.reset_in = limit, spent, reset
        self.updated = time.time()

    def summary(self) -> str:
        if self.limit is None:
            return "rate limit unknown"
        return (f"points {self.spent:.0f}/{self.limit:.0f}, reset in {int(self.reset_in or 0)} s, "
                f"cost/page ~{self.cost:.1f} ({self.measured} measured)")

    def wait_needed(self, next_cost: float | None = None) -> float:
        """Seconds to wait before the next request, zero when none."""
        if self.limit is None or self.spent is None:
            return 0.0
        cost = next_cost if next_cost is not None else self.cost
        headroom = max(self.margin, 2.0 * cost, 25.0)
        elapsed = (time.time() - self.updated) if self.updated else 0.0
        reset = max(0.0, (self.reset_in or 0.0) - elapsed)
        if self.spent + cost + headroom > self.limit:
            return reset + 5.0
        return 0.0

    def before_request(self) -> None:
        w = self.wait_needed()
        if w > 0:
            self.log(f"  rate limit: {self.summary()}; waiting {int(w)} s for the hourly reset")
            self.sleep(w)
            # after the reset the spent counter is zero
            self.spent = 0.0
            self.reset_in = 3600.0
            self.updated = time.time()


# ---------------------------------------------------------------------------
# API client
# ---------------------------------------------------------------------------

class WclClient:
    def __init__(self, client_id: str, client_secret: str, limiter: RateLimiter, log=print, sleep=time.sleep, max_attempts: int = 6, post=None):
        self._id = client_id
        self._secret = client_secret
        self._token = None
        self.limiter = limiter
        self.log = log
        self.sleep = sleep
        self.max_attempts = max_attempts
        self.requests_made = 0
        self.post = post or http_post  # injectable transport; the dry run passes a fake

    def token(self) -> str:
        if self._token:
            return self._token
        basic = base64.b64encode(f"{self._id}:{self._secret}".encode("utf-8")).decode("ascii")
        headers = {"Authorization": f"Basic {basic}", "Content-Type": "application/x-www-form-urlencoded",
                   "Accept": "application/json", "User-Agent": USER_AGENT}
        body = b"grant_type=client_credentials"
        last = None
        for attempt in range(1, self.max_attempts + 1):
            try:
                r = self.post(TOKEN_URL, headers, body, timeout=30)
            except Exception as e:  # network error
                last = f"network error: {type(e).__name__}"
                self._backoff(attempt, last)
                continue
            if r.status == 200:
                data = r.json() or {}
                tok = data.get("access_token")
                if not tok:
                    raise FatalError("token endpoint answered 200 without an access_token")
                self._token = tok
                self.log(f"  token obtained (type {data.get('token_type', '?')}, expires in {data.get('expires_in', '?')} s)")
                return tok
            if r.status in (400, 401, 403):
                raise FatalError(f"token endpoint refused the client credentials (HTTP {r.status}); check WCL_CLIENT_ID and WCL_CLIENT_SECRET")
            last = f"HTTP {r.status} from token endpoint"
            self._backoff(attempt, last)
        raise FatalError(f"could not obtain a token: {last}")

    def _backoff(self, attempt: int, why: str, base: float = 2.0) -> None:
        if attempt >= self.max_attempts:
            return
        wait = min(120.0, base * (2 ** (attempt - 1))) + random.uniform(0, 1.0)
        self.log(f"  {why}; retry {attempt}/{self.max_attempts - 1} in {wait:.0f} s")
        self.sleep(wait)

    def graphql(self, host: str, query: str, variables: dict | None = None, measure_cost: bool = False) -> dict:
        """POSTs a query and returns the parsed body. Handles rate limits and retries."""
        url = f"https://{host}/api/v2/client"
        payload = json.dumps({"query": query, "variables": variables or {}}).encode("utf-8")
        last = None
        throttled = 0
        for attempt in range(1, self.max_attempts + 1):
            self.limiter.before_request()
            headers = {"Authorization": f"Bearer {self.token()}", "Content-Type": "application/json",
                       "Accept": "application/json", "User-Agent": USER_AGENT}
            try:
                r = self.post(url, headers, payload, timeout=90)
                self.requests_made += 1
            except Exception as e:
                last = f"network error: {type(e).__name__}"
                self._backoff(attempt, last)
                continue
            if r.status == 401:
                # token expired or revoked: fetch a new one once
                self._token = None
                last = "HTTP 401; refreshing token"
                self._backoff(attempt, last, base=1.0)
                continue
            if r.status == 429:
                throttled += 1
                if throttled > 12:
                    raise TransientError(f"{host} answered 429 twelve times in a row")
                wait = _retry_after(r) or (self.limiter.reset_in or 60.0) + 5.0
                self.log(f"  HTTP 429; waiting {int(wait)} s")
                self.sleep(wait)
                continue
            if r.status >= 500 or r.status in (408,):
                last = f"HTTP {r.status}"
                self._backoff(attempt, last)
                continue
            if r.status != 200:
                raise FatalError(f"HTTP {r.status} from {host}: {r.text[:300]}")
            try:
                body = r.json()
            except Exception:
                last = "unparseable body"
                self._backoff(attempt, last)
                continue
            data = body.get("data") or {}
            self.limiter.update(data.get("rateLimitData"), measure=measure_cost)
            errors = body.get("errors") or []
            if errors:
                msgs = "; ".join(str(e.get("message", e)) for e in errors)
                if re.search(r"rate limit|too many", msgs, re.I):
                    wait = (self.limiter.reset_in or 60.0) + 5.0
                    self.log(f"  API reports rate limiting; waiting {int(wait)} s")
                    self.sleep(wait)
                    continue
                if re.search(r"internal|timeout|temporar|unavailable", msgs, re.I):
                    last = f"GraphQL error: {msgs[:200]}"
                    self._backoff(attempt, last)
                    continue
                raise FatalError(f"GraphQL error from {host}: {msgs[:500]}")
            return body
        raise TransientError(f"gave up on {host} after {self.max_attempts} attempts: {last}")


def _retry_after(r: HttpResponse) -> float | None:
    v = r.headers.get("retry-after")
    if not v:
        return None
    try:
        return float(v)
    except ValueError:
        return None


# ---------------------------------------------------------------------------
# Plan
# ---------------------------------------------------------------------------

def build_plan(args, root: Path) -> dict:
    sources = [s for s in args.sources.split(",") if s]
    for s in sources:
        if s not in SOURCES:
            raise SystemExit(f"unknown source {s!r}; known: {', '.join(SOURCES)}")
    encounters = [e for e in (args.encounters.split(",") if args.encounters else ENCOUNTERS)]
    for e in encounters:
        if e not in ENCOUNTERS:
            raise SystemExit(f"unknown encounter key {e!r}; known: {', '.join(ENCOUNTERS)}")
    specs = dict(SPECS)
    if args.no_thin:
        specs = {k: v for k, v in specs.items() if v[2] != "thin"}
    if args.specs:
        chosen = {}
        for token in args.specs.split(","):
            token = token.strip()
            if not token:
                continue
            if token in specs:
                chosen[token] = specs[token]
            elif "/" in token:
                cls, spec = token.split("/", 1)
                key = f"{cls.lower()}-{spec.lower()}"
                chosen[key] = (cls, spec, "custom")
            else:
                raise SystemExit(f"unknown spec {token!r}; use a known key or Class/Spec")
        specs = chosen
    cells = []
    for src in sources:
        for enc in encounters:
            for key, (cls, spec, group) in specs.items():
                metrics = ["hps"] if group == "healer" else ["dps"]
                if group != "healer" and enc in CLEAVE_ENCOUNTERS:
                    metrics.append("bossdps")
                if args.metrics:
                    metrics = [m for m in metrics if m in args.metrics.split(",")]
                for m in metrics:
                    cells.append({
                        "id": f"{src}/{enc}/{key}/{m}",
                        "source": src, "encounterKey": enc, "specKey": key,
                        "className": cls, "specName": spec, "group": group, "metric": m,
                    })
    return {
        "root": str(root),
        "sources": sources,
        "encounters": encounters,
        "specs": specs,
        "cells": cells,
        "percentiles": list(PERCENTILES),
        "windowDays": args.window_days,
        "maxPages": args.max_pages,
    }


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

def choose_zone(zones: list, memo_id: int | None, log) -> dict | None:
    cands = [z for z in zones if re.search(r"naxx", z.get("name", ""), re.I)]
    if not cands:
        return None
    if memo_id is not None and any(z.get("id") == memo_id for z in cands):
        pick = next(z for z in cands if z.get("id") == memo_id)
    else:
        pick = max(cands, key=lambda z: z.get("id") or 0)
    if len(cands) > 1:
        log("  more than one Naxxramas zone: " + ", ".join(f"{z['id']} {z['name']}" for z in cands) + f"; using {pick['id']}")
    return pick


def choose_partition(zone: dict, matcher: str | None, override: int | None, log) -> dict | None:
    parts = zone.get("partitions") or []
    if override is not None:
        for p in parts:
            if p.get("id") == override:
                return p
        log(f"  partition override {override} is not listed for zone {zone.get('id')}; using it anyway")
        return {"id": override, "name": f"override {override}", "compactName": None, "default": None}
    if matcher:
        m = [p for p in parts if re.search(matcher, p.get("name") or "", re.I) or re.search(matcher, p.get("compactName") or "", re.I)]
        if m:
            return max(m, key=lambda p: p.get("id") or 0)
        return None
    d = [p for p in parts if p.get("default")]
    if d:
        return d[0]
    if parts:
        return max(parts, key=lambda p: p.get("id") or 0)
    return None


def match_encounters(zone: dict, keys: list, log) -> dict:
    out = {}
    encs = zone.get("encounters") or []
    for key in keys:
        pat, expected = ENCOUNTERS[key][0], ENCOUNTERS[key][1]
        m = [e for e in encs if re.search(pat, e.get("name", ""), re.I)]
        if not m:
            out[key] = None
            log(f"  encounter {key}: expected '{expected}', no match in zone {zone.get('id')}")
        else:
            if len(m) > 1:
                log(f"  encounter {key}: several matches, using the first: " + ", ".join(f"{e['id']} {e['name']}" for e in m))
            out[key] = {"id": m[0]["id"], "name": m[0]["name"]}
            log(f"  encounter {key}: expected '{expected}', found {m[0]['id']} '{m[0]['name']}'")
    return out


def verify_specs(classes: list, specs: dict, log) -> dict:
    """Checks each planned class and spec against gameData.classes.

    Returns {specKey: {"note": str, "useSpecName": str | None}} for every spec
    that did not match exactly; useSpecName carries a corrected name when one
    was found by a case-insensitive or de-spaced match.
    """
    by_class = {}
    for c in classes or []:
        by_class[c.get("name", "").lower()] = {s.get("name"): s for s in (c.get("specs") or [])}
    notes = {}
    if not by_class:
        log("  spec check: gameData.classes returned nothing; plan names are used as written")
        return notes
    for key, (cls, spec, group) in specs.items():
        cspecs = by_class.get(cls.lower())
        if cspecs is None:
            notes[key] = {"note": f"class {cls} not listed by gameData.classes", "useSpecName": None}
            continue
        if spec in cspecs:
            continue
        alt = [n for n in cspecs if n and n.replace(" ", "").lower() == spec.replace(" ", "").lower()]
        if alt:
            notes[key] = {"note": f"spec name is {alt[0]!r} on this host, plan says {spec!r}; using the host's", "useSpecName": alt[0]}
        else:
            notes[key] = {"note": f"spec {spec} not listed for {cls}; listed: {', '.join(n for n in cspecs if n)}", "useSpecName": None}
    for key, n in notes.items():
        log(f"  spec check {key}: {n['note']}")
    if not notes:
        log(f"  spec check: all {len(specs)} planned class and spec names are listed by gameData.classes")
    return notes


def run_discovery(client: WclClient, plan: dict, args, paths: dict, log) -> dict:
    ids = {"discoveredAt": now_iso(), "tool": f"tools/wcl_pull.py {VERSION}", "sources": {}}
    for src in plan["sources"]:
        S = SOURCES[src]
        host = args.host_override.get(src, S["host"])
        log(f"discovery on {host} ({S['label']})")
        body = client.graphql(host, Q_DISCOVERY)
        data = body.get("data") or {}
        world = data.get("worldData") or {}
        zones = world.get("zones") or []
        log(f"  {len(zones)} zones listed:")
        for z in zones:
            exp = (z.get("expansion") or {}).get("name")
            log(f"    zone {z.get('id'):>5}  {z.get('name')}  [{exp}]  partitions {len(z.get('partitions') or [])}  encounters {len(z.get('encounters') or [])}  frozen {z.get('frozen')}")
        zone_override = args.zone_override.get(src)
        if zone_override is not None:
            zone = next((z for z in zones if z.get("id") == zone_override), None)
            if zone is None:
                raise FatalError(f"zone override {zone_override} not listed on {host}")
        else:
            zone = choose_zone(zones, S["memoZoneId"], log)
        if zone is None:
            raise FatalError(f"no Naxxramas zone found on {host}; pass --zone {src}=ID")
        memo_ok = zone.get("id") == S["memoZoneId"]
        log(f"  Naxxramas zone: {zone['id']} {zone['name']} (memo said {S['memoZoneId']}: {'agrees' if memo_ok else 'DIFFERS'})")
        log("  partitions:")
        for p in zone.get("partitions") or []:
            log(f"    partition {p.get('id'):>4}  {p.get('name')}  compact {p.get('compactName')}  default {p.get('default')}")
        part = choose_partition(zone, S["partitionMatch"], args.partition_override.get(src), log)
        if part is None:
            raise FatalError(f"no partition matched for {src} on {host} ({S['partitionRule']}); pass --partition {src}=ID")
        log(f"  chosen partition: {part.get('id')} {part.get('name')} ({S['partitionRule']})")
        log("  encounters:")
        for e in zone.get("encounters") or []:
            log(f"    encounter {e.get('id'):>5}  {e.get('name')}")
        encs = match_encounters(zone, plan["encounters"], log)
        game = data.get("gameData") or {}
        spec_notes = verify_specs(game.get("classes") or [], plan["specs"], log)
        factions = {str(f.get("id")): f.get("name") for f in (game.get("factions") or [])}
        if factions:
            log("  factions: " + ", ".join(f"{k}={v}" for k, v in factions.items()))
        ids["sources"][src] = {
            "label": S["label"], "host": host, "endpoint": f"https://{host}/api/v2/client",
            "zone": {"id": zone.get("id"), "name": zone.get("name"), "frozen": zone.get("frozen"), "memoZoneId": S["memoZoneId"], "memoAgrees": memo_ok},
            "zonesListed": [{"id": z.get("id"), "name": z.get("name")} for z in zones],
            "partition": {"id": part.get("id"), "name": part.get("name"), "compactName": part.get("compactName"), "default": part.get("default"), "rule": S["partitionRule"]},
            "partitionsListed": zone.get("partitions") or [],
            "encounters": encs,
            "encountersListed": zone.get("encounters") or [],
            "classes": game.get("classes") or [],
            "specNotes": spec_notes,
            "factions": factions,
            "rateLimit": data.get("rateLimitData"),
        }
        log(f"  {client.limiter.summary()}")
    write_json_atomic(paths["ids"], ids)
    log(f"wrote {paths['ids']}")
    return ids


# ---------------------------------------------------------------------------
# Pull
# ---------------------------------------------------------------------------

def cache_path(paths: dict, cell: dict, page: int) -> Path:
    return paths["raw"] / cell["source"] / cell["encounterKey"] / f"{cell['specKey']}-{cell['metric']}" / f"page-{page:03d}.json"


CACHE_KEYS = ("encounter", "className", "specName", "metric", "partition", "page")


def cached_page(paths: dict, cell: dict, page: int, variables: dict | None = None) -> dict | None:
    """Returns the cached page when it exists, succeeded, and was produced by the same variables."""
    p = cache_path(paths, cell, page)
    doc = read_json(p)
    if not doc:
        return None
    resp = doc.get("response") or {}
    if resp.get("errors"):
        return None
    if variables is not None:
        have = doc.get("variables") or {}
        if any(have.get(k) != variables.get(k) for k in CACHE_KEYS):
            return None
    return doc


def prune_pages(paths: dict, cell: dict, keep: int) -> int:
    """Removes cached pages beyond `keep` so a shorter refetch cannot leave stale tails."""
    d = cache_path(paths, cell, 1).parent
    removed = 0
    if not d.exists():
        return 0
    for p in d.glob("page-*.json"):
        try:
            n = int(p.stem.split("-")[1])
        except (IndexError, ValueError):
            continue
        if n > keep:
            p.unlink()
            removed += 1
    return removed


def rankings_from(doc: dict) -> dict | None:
    try:
        return ((doc.get("response") or {}).get("data") or {}).get("worldData", {}).get("encounter", {}).get("characterRankings")
    except AttributeError:
        return None


def pull_cell(client: WclClient, cell: dict, ids: dict, plan: dict, args, paths: dict, progress: dict, log) -> dict:
    src = ids["sources"][cell["source"]]
    enc = src["encounters"].get(cell["encounterKey"])
    if not enc:
        log(f"  {cell['id']}: encounter not found on host; skipped")
        return {"pages": 0, "complete": False, "reason": "encounter not found"}
    partition = src["partition"]["id"]
    host = src["host"]
    spec_note = (src.get("specNotes") or {}).get(cell["specKey"]) or {}
    spec_name = spec_note.get("useSpecName") or cell["specName"]
    page = 1
    pages_done = 0
    fetched = 0
    total = None
    while True:
        if plan["maxPages"] and page > plan["maxPages"]:
            log(f"  {cell['id']}: stopped at --max-pages {plan['maxPages']}; not recorded as complete")
            return {"pages": pages_done, "complete": False, "reason": "max-pages", "count": total}
        variables = {"encounter": enc["id"], "className": cell["className"], "specName": spec_name,
                     "metric": cell["metric"], "partition": partition, "page": page, "combatant": page == 1}
        doc = None if args.refresh else cached_page(paths, cell, page, variables)
        if doc is None:
            body = client.graphql(host, Q_RANKINGS, variables, measure_cost=True)
            doc = {"pulledAt": now_iso(), "host": host, "endpoint": f"https://{host}/api/v2/client",
                   "operation": "Rankings", "queryHash": qhash(Q_RANKINGS), "query": Q_RANKINGS,
                   "variables": variables, "rateLimit": (body.get("data") or {}).get("rateLimitData"),
                   "response": body}
            write_json_atomic(cache_path(paths, cell, page), doc)
            fetched += 1
        rk = rankings_from(doc)
        if not isinstance(rk, dict):
            log(f"  {cell['id']}: page {page} returned no rankings object (partition {partition} may not apply here)")
            return {"pages": pages_done, "complete": False, "reason": "no rankings object"}
        pages_done += 1
        total = rk.get("count", total)
        if not rk.get("hasMorePages"):
            break
        page += 1
    pruned = prune_pages(paths, cell, pages_done)
    if pruned:
        log(f"  {cell['id']}: removed {pruned} stale cached pages beyond page {pages_done}")
    entry = {"pages": pages_done, "complete": True, "count": total, "fetched": fetched, "finishedAt": now_iso()}
    progress.setdefault("cells", {})[cell["id"]] = entry
    write_json_atomic(paths["progress"], progress)
    return entry


def run_pull(client: WclClient, plan: dict, ids: dict, args, paths: dict, log) -> None:
    progress = read_json(paths["progress"], {"cells": {}}) if args.resume else {"cells": {}}
    n = len(plan["cells"])
    log(f"pull: {n} cells; {client.limiter.summary()}")
    for i, cell in enumerate(plan["cells"], 1):
        prev = progress.get("cells", {}).get(cell["id"])
        if args.resume and prev and prev.get("complete") and not args.refresh:
            log(f"[{i}/{n}] {cell['id']}: complete in progress file ({prev.get('pages')} pages); skipped")
            continue
        t0 = time.time()
        try:
            res = pull_cell(client, cell, ids, plan, args, paths, progress, log)
        except TransientError as e:
            log(f"[{i}/{n}] {cell['id']}: {e}; moving on, rerun with --resume to retry")
            continue
        log(f"[{i}/{n}] {cell['id']}: {res.get('pages')} pages, {res.get('fetched', 0)} fetched, count {res.get('count')}, "
            f"{time.time() - t0:.0f} s; {client.limiter.summary()}")


# ---------------------------------------------------------------------------
# Reduce
# ---------------------------------------------------------------------------

def load_cell_rankings(paths: dict, cell: dict) -> tuple[list, list, dict | None]:
    """Returns (rankings, raw file names, first page doc)."""
    d = cache_path(paths, cell, 1).parent
    rows, files, first = [], [], None
    if not d.exists():
        return rows, files, first
    for p in sorted(d.glob("page-*.json")):
        doc = read_json(p)
        if not doc:
            continue
        rk = rankings_from(doc)
        if not isinstance(rk, dict):
            continue
        if first is None:
            first = doc
        files.append(str(p.relative_to(paths["controls"])).replace("\\", "/"))
        rows.extend(rk.get("rankings") or [])
    return rows, files, first


def ranking_start_ms(r: dict):
    st = r.get("startTime")
    if st is None:
        st = (r.get("report") or {}).get("startTime")
    return st


def faction_of(r: dict, factions: dict) -> str:
    f = r.get("faction")
    if f is None:
        f = (r.get("guild") or {}).get("faction")
    if isinstance(f, dict):
        f = f.get("name") or f.get("id")
    name = factions.get(str(f)) if factions else None
    return name or (str(f) if f is not None else "unknown")


def reduce_cells(plan: dict, ids: dict, paths: dict, args, log) -> dict:
    """Builds controls.json content from the raw cache."""
    generated = now_iso()
    out = {
        "title": "Warcraft Logs controls, Naxxramas",
        "generated": generated,
        "tool": f"tools/wcl_pull.py {VERSION}",
        "method": {
            "query": "worldData.encounter(id).characterRankings(className, specName, metric, partition, page, includeCombatantInfo)",
            "queryHash": qhash(Q_RANKINGS),
            "pool": "each character's best kill per encounter per partition, all pages",
            "window": f"kills whose start time falls in the last {plan['windowDays']} days of the partition's observed activity, or before an explicit --window-end",
            "percentiles": "nearest rank on amounts within the window",
            "combatantInfo": "page one of every cell carries gear and talents",
        },
        "sources": {},
        "encounters": {},
        "cells": [],
        "derived": [],
    }
    for src in plan["sources"]:
        S = ids["sources"][src]
        out["sources"][src] = {
            "label": S["label"], "host": S["host"], "endpoint": S["endpoint"],
            "zoneId": S["zone"]["id"], "zoneName": S["zone"]["name"],
            "partitionId": S["partition"]["id"], "partitionName": S["partition"]["name"],
            "worldBuffs": SOURCES[src]["worldBuffs"], "note": SOURCES[src]["note"],
        }
    for key in plan["encounters"]:
        pat, expected, scenario, role = ENCOUNTERS[key]
        out["encounters"][key] = {"expectedName": expected, "scenario": scenario, "role": role, "ids": {
            src: (ids["sources"][src]["encounters"].get(key) or {}).get("id") for src in plan["sources"]}}

    # First pass: gather rankings per cell and find each source's newest kill.
    gathered = {}
    newest = {src: None for src in plan["sources"]}
    for cell in plan["cells"]:
        rows, files, first = load_cell_rankings(paths, cell)
        gathered[cell["id"]] = (rows, files, first)
        for r in rows:
            st = ranking_start_ms(r)
            if st is not None and (newest[cell["source"]] is None or st > newest[cell["source"]]):
                newest[cell["source"]] = st

    windows = {}
    for src in plan["sources"]:
        end_override = args.window_end.get(src)
        if end_override:
            end_ms = int(parse_date(end_override).timestamp() * 1000) + 24 * 3600 * 1000 - 1
            basis = f"--window-end {end_override}"
        elif newest[src] is not None:
            end_ms = newest[src]
            basis = "newest ranking start time observed in the pull"
        else:
            end_ms = None
            basis = "no rankings pulled"
        start_ms = (end_ms - plan["windowDays"] * 86400 * 1000) if end_ms is not None else None
        windows[src] = {"startMs": start_ms, "endMs": end_ms, "start": ms_to_iso(start_ms), "end": ms_to_iso(end_ms), "days": plan["windowDays"], "basis": basis}
        out["sources"][src]["window"] = windows[src]

    factions_by_src = {src: ids["sources"][src].get("factions") or {} for src in plan["sources"]}

    for cell in plan["cells"]:
        rows, files, first = gathered[cell["id"]]
        src = cell["source"]
        w = windows[src]
        enc = ids["sources"][src]["encounters"].get(cell["encounterKey"]) or {}
        in_win = [r for r in rows if w["startMs"] is None or (ranking_start_ms(r) is not None and w["startMs"] <= ranking_start_ms(r) <= w["endMs"])]
        amounts = sorted(float(r.get("amount") or 0.0) for r in in_win)
        durations = sorted((r.get("duration") or 0) / 1000.0 for r in in_win)
        fac = {}
        for r in in_win:
            f = faction_of(r, factions_by_src[src])
            fac[f] = fac.get(f, 0) + 1
        pulled_at = (first or {}).get("pulledAt")
        prov_base = {"query": "Rankings", "queryHash": qhash(Q_RANKINGS), "host": ids["sources"][src]["host"],
                     "partition": ids["sources"][src]["partition"]["id"], "encounterId": enc.get("id"),
                     "className": cell["className"], "specName": (first or {}).get("variables", {}).get("specName", cell["specName"]),
                     "metric": cell["metric"], "pulledAt": pulled_at}
        pct = {}
        for p in PERCENTILES:
            v, k = nearest_rank(amounts, p)
            pct[str(p)] = {"amount": (round(v, 1) if v is not None else None), "rank": k, "n": len(amounts),
                           "provenance": dict(prov_base, percentile=p, timestamp=pulled_at)}
        dur = {str(p): (round(nearest_rank(durations, p)[0], 1) if durations else None) for p in (25, 50, 75)}
        entry = {
            "id": cell["id"], "source": src, "encounterKey": cell["encounterKey"], "encounterId": enc.get("id"), "encounterName": enc.get("name"),
            "specKey": cell["specKey"], "className": cell["className"], "specName": cell["specName"], "group": cell["group"], "metric": cell["metric"],
            "partition": ids["sources"][src]["partition"]["id"],
            "sampleAll": len(rows), "sampleInWindow": len(amounts), "pages": len(files),
            "thin": len(amounts) < THIN_SAMPLE,
            "percentiles": pct,
            "durationSeconds": dur,
            "faction": fac,
            "rawFiles": files,
            "combatantInfoOnPageOne": bool(first and (first.get("variables") or {}).get("combatant")),
        }
        if cell["encounterKey"] == "patchwerk" and cell["metric"] == "dps" and in_win:
            q = nearest_rank(durations, 25)[0]
            short = sorted(float(r.get("amount") or 0.0) for r in in_win if (r.get("duration") or 0) / 1000.0 <= q)
            entry["burstProxyUnvalidated"] = {
                "note": "shortest-duration quartile of Patchwerk kills; not a forty-five second fight and not a control",
                "durationCutoffSeconds": round(q, 1), "n": len(short),
                **{str(p): (round(nearest_rank(short, p)[0], 1) if short else None) for p in PERCENTILES},
            }
        out["cells"].append(entry)

    # Derived: add damage on the cleave encounters as dps minus bossdps per percentile.
    by_id = {c["id"]: c for c in out["cells"]}
    for c in out["cells"]:
        if c["metric"] != "dps" or c["encounterKey"] not in CLEAVE_ENCOUNTERS:
            continue
        b = by_id.get(c["id"].rsplit("/", 1)[0] + "/bossdps")
        if not b:
            continue
        diff = {}
        for p in PERCENTILES:
            a = c["percentiles"][str(p)]["amount"]
            bb = b["percentiles"][str(p)]["amount"]
            diff[str(p)] = round(a - bb, 1) if (a is not None and bb is not None) else None
        out["derived"].append({
            "id": c["id"].rsplit("/", 1)[0] + "/dps-minus-bossdps",
            "source": c["source"], "encounterKey": c["encounterKey"], "specKey": c["specKey"], "group": c["group"],
            "className": c["className"], "specName": c["specName"],
            "note": "difference of percentiles, not the percentile of per-character differences; the two pools may be different kills",
            "addDamage": diff, "n": {"dps": c["sampleInWindow"], "bossdps": b["sampleInWindow"]},
        })
    return out


# ---------------------------------------------------------------------------
# Render (auditor register)
# ---------------------------------------------------------------------------

def _cell_text(c: dict | None) -> str:
    if c is None:
        return "not pulled"
    if c["sampleAll"] == 0:
        return "no rankings"
    if c["sampleInWindow"] == 0:
        return f"none in window ({c['sampleAll']} pulled)"
    p = c["percentiles"]
    s = f"{fmt_int(p['75']['amount'])} ({fmt_int(p['50']['amount'])} to {fmt_int(p['95']['amount'])}, n={c['sampleInWindow']})"
    if c["thin"]:
        s += " thin"
    return s


def render_md(ctl: dict, plan: dict, synthetic: bool = False) -> str:
    L = []
    L.append("# Warcraft Logs controls")
    L.append("")
    if synthetic:
        L.append("Dry run on synthetic data. No number below came from Warcraft Logs; the table exists to prove the reduce and render paths.")
        L.append("")
    L.append(f"Generated {ctl['generated']} by `tools/wcl_pull.py`. The pull follows `absolute-numbers.md` sections 4 and 6. Every number is a percentile of the amounts Warcraft Logs returns from `worldData.encounter.characterRankings`, one best kill per character per partition, restricted to kills that started inside the window. Percentiles use the nearest-rank method. The 75th percentile leads and the 50th and 95th follow in brackets. Cells with fewer than {THIN_SAMPLE} rankings in the window are marked thin and should be read as such rather than dropped.")
    L.append("")
    L.append("## Sources")
    L.append("")
    L.append("| Source | Host | Zone | Partition | Window | World buffs |")
    L.append("|---|---|---|---|---|---|")
    for key, s in ctl["sources"].items():
        w = s.get("window") or {}
        L.append(f"| {s['label']} | `{s['host']}` | {s['zoneId']} {s['zoneName']} | {s['partitionId']} {s['partitionName']} | {(w.get('start') or '-')[:10]} to {(w.get('end') or '-')[:10]} ({w.get('days')} days; {w.get('basis')}) | {'yes' if s['worldBuffs'] else 'no'} |")
    L.append("")
    enc_keys = [k for k in ENCOUNTERS if k in ctl["encounters"]]
    enc_names = {k: (next((c["encounterName"] for c in ctl["cells"] if c["encounterKey"] == k and c.get("encounterName")), None) or ctl["encounters"][k].get("expectedName") or k) for k in enc_keys}
    cells = ctl["cells"]

    def table(src: str, group_filter, metric: str, title: str):
        rows = [c for c in cells if c["source"] == src and c["metric"] == metric and group_filter(c["group"])]
        if not rows:
            return
        L.append(f"### {title}")
        L.append("")
        L.append("| Spec | " + " | ".join(enc_names[k] for k in enc_keys) + " |")
        L.append("|---|" + "---|" * len(enc_keys))
        seen = []
        for c in rows:
            if c["specKey"] not in seen:
                seen.append(c["specKey"])
        idx = {(c["specKey"], c["encounterKey"]): c for c in rows}
        for sk in seen:
            cls, spec = next((c["className"], c["specName"]) for c in rows if c["specKey"] == sk)
            L.append(f"| {cls} {spec} | " + " | ".join(_cell_text(idx.get((sk, k))) for k in enc_keys) + " |")
        L.append("")

    for src, s in ctl["sources"].items():
        if not any(c["source"] == src for c in cells):
            L.append(f"## {s['label']}")
            L.append("")
            L.append("No cells were pulled for this source.")
            L.append("")
            continue
        L.append(f"## {s['label']}")
        L.append("")
        table(src, lambda g: g in ("dps", "custom"), "dps", "Damage, dps, 75th percentile (50th to 95th, n)")
        table(src, lambda g: g == "thin", "dps", "Thin specs, dps")
        table(src, lambda g: g == "healer", "hps", "Healing, hps")

    if ctl.get("derived"):
        L.append("## Add damage on the cleave encounters")
        L.append("")
        L.append("Difference of the dps and bossdps percentiles per spec. It is not the percentile of per-character differences, and the two pools may be different kills, so read it as the size of the add contribution rather than as a ranking.")
        L.append("")
        L.append("| Source | Encounter | Spec | p50 | p75 | p95 | n (dps, bossdps) |")
        L.append("|---|---|---|---|---|---|---|")
        for d in ctl["derived"]:
            L.append(f"| {ctl['sources'][d['source']]['label']} | {enc_names.get(d['encounterKey'], d['encounterKey'])} | {d.get('className', '')} {d.get('specName', d['specKey'])} | {fmt_int(d['addDamage']['50'])} | {fmt_int(d['addDamage']['75'])} | {fmt_int(d['addDamage']['95'])} | {d['n']['dps']}, {d['n']['bossdps']} |")
        L.append("")

    burst = [c for c in cells if c.get("burstProxyUnvalidated")]
    if burst:
        L.append("## Burst proxy, unvalidated")
        L.append("")
        L.append("The shortest-duration quartile of Patchwerk kills, at the same percentiles. The memo reports burst as unvalidated and this table does not change that; a two-minute kill is not a forty-five second fight.")
        L.append("")
        L.append("| Source | Spec | Cutoff (s) | n | p50 | p75 | p95 |")
        L.append("|---|---|---|---|---|---|---|")
        for c in burst:
            b = c["burstProxyUnvalidated"]
            L.append(f"| {ctl['sources'][c['source']]['label']} | {c['className']} {c['specName']} | {b['durationCutoffSeconds']} | {b['n']} | {fmt_int(b['50'])} | {fmt_int(b['75'])} | {fmt_int(b['95'])} |")
        L.append("")

    L.append("## Durations and factions")
    L.append("")
    L.append("Median kill duration in seconds and the faction split of the rankings in the window, per source and encounter, taken from the dps cells summed across specs.")
    L.append("")
    L.append("| Source | Encounter | Median duration (s) | Rankings | Faction split |")
    L.append("|---|---|---|---|---|")
    for src, s in ctl["sources"].items():
        for k in enc_keys:
            rows = [c for c in cells if c["source"] == src and c["encounterKey"] == k and c["metric"] == "dps"]
            if not rows:
                continue
            meds = [c["durationSeconds"]["50"] for c in rows if c["durationSeconds"]["50"] is not None]
            med = sorted(meds)[len(meds) // 2] if meds else None
            n = sum(c["sampleInWindow"] for c in rows)
            fac = {}
            for c in rows:
                for f, v in c["faction"].items():
                    fac[f] = fac.get(f, 0) + v
            fs = ", ".join(f"{f} {v}" for f, v in sorted(fac.items())) or "-"
            L.append(f"| {s['label']} | {enc_names[k]} | {fmt_int(med) if med is not None else '-'} | {n} | {fs} |")
    L.append("")

    thin = [c for c in cells if c["thin"]]
    L.append("## Thin cells")
    L.append("")
    if thin:
        L.append(f"{len(thin)} of {len(cells)} cells hold fewer than {THIN_SAMPLE} rankings in the window: " + ", ".join(f"`{c['id']}` ({c['sampleInWindow']})" for c in thin) + ".")
    else:
        L.append(f"Every cell holds at least {THIN_SAMPLE} rankings in the window.")
    L.append("")
    L.append("## Provenance")
    L.append("")
    L.append(f"Query `Rankings`, hash `{ctl['method']['queryHash']}`, text in `tools/wcl_pull.py`. Raw responses with the variables that produced them sit under `files/controls/raw/` and are listed per cell in `controls.json`. Zone, partition and encounter identifiers were read from `worldData` at pull time and are recorded in `files/controls/wcl-ids.json`. Combatant info is on page one of every cell.")
    L.append("")
    return "\n".join(L)


def write_outputs(ctl: dict, plan: dict, paths: dict, log, synthetic: bool = False) -> None:
    write_json_atomic(paths["controls_json"], ctl)
    md = render_md(ctl, plan, synthetic=synthetic)
    paths["controls_md"].parent.mkdir(parents=True, exist_ok=True)
    with open(paths["controls_md"], "w", encoding="utf-8", newline="\n") as fh:
        fh.write(md)
    log(f"wrote {paths['controls_json']}")
    log(f"wrote {paths['controls_md']}")


# ---------------------------------------------------------------------------
# Dry run
# ---------------------------------------------------------------------------

def dry_run_subset(plan: dict) -> list:
    """A mixed slice of the plan so the offline pull and reduce touch every branch."""
    wanted = set()
    for src in plan["sources"]:
        wanted.update({
            f"{src}/patchwerk/warrior-fury/dps", f"{src}/patchwerk/rogue-combat/dps", f"{src}/patchwerk/mage-frost/dps",
            f"{src}/heigan/warrior-fury/dps",
            f"{src}/faerlina/warrior-fury/dps", f"{src}/faerlina/warrior-fury/bossdps",
            f"{src}/patchwerk/hunter-survival/dps", f"{src}/patchwerk/priest-holy/hps",
        })
    subset = [c for c in plan["cells"] if c["id"] in wanted]
    return subset or plan["cells"][:12]


class FakeTransport:
    """An in-memory stand-in for the two Warcraft Logs endpoints.

    It answers the token endpoint, Discovery, RateLimit and Rankings with
    plausible shapes, and injects one of each fault the client is built to
    survive: a 500 on the first token call, then a 401, a 429, a 500 and a
    GraphQL rate-limit error on the first four rankings calls. Nothing here
    is real data and nothing leaves the process.
    """

    NEWEST = {"vanilla.warcraftlogs.com": _dt.datetime(2023, 2, 14, tzinfo=_dt.timezone.utc),
              "fresh.warcraftlogs.com": _dt.datetime(2026, 8, 10, tzinfo=_dt.timezone.utc)}
    SIZES = [0, 12, 60, 240, 130, 45, 300, 8, 175, 26, 7, 33]
    BOSSES = ["Anub'Rekhan", "Grand Widow Faerlina", "Maexxna", "Noth the Plaguebringer", "Heigan the Unclean", "Loatheb",
              "Instructor Razuvious", "Gothik the Harvester", "The Four Horsemen", "Patchwerk", "Grobbulus", "Gluth",
              "Thaddius", "Sapphiron", "Kel'Thuzad"]
    CLASSES = [("Warrior", ["Arms", "Fury", "Protection"]), ("Rogue", ["Assassination", "Combat", "Subtlety"]),
               ("Mage", ["Arcane", "Fire", "Frost"]), ("Warlock", ["Affliction", "Demonology", "Destruction"]),
               ("Hunter", ["BeastMastery", "Marksmanship", "Survival"]), ("Druid", ["Balance", "Feral", "Guardian", "Restoration"]),
               ("Shaman", ["Elemental", "Enhancement", "Restoration"]), ("Priest", ["Discipline", "Holy", "Shadow"]),
               ("Paladin", ["Holy", "Protection", "Retribution"])]

    def __init__(self, log):
        self.log = log
        self.calls = 0
        self.token_calls = 0
        self.rankings_calls = 0
        self.spent = 40.0
        self.faults = ["401", "429", "500", "gql-rate"]

    def _zone_doc(self, host: str) -> dict:
        if host.startswith("vanilla"):
            zones = [
                {"id": 2005, "name": "Temple of Ahn'Qiraj", "frozen": True, "expansion": {"id": 1, "name": "Classic Era"}, "partitions": [], "encounters": []},
                {"id": 2006, "name": "Naxxramas", "frozen": False, "expansion": {"id": 1, "name": "Classic Era"},
                 "partitions": [{"id": 1, "name": "Classic Era", "compactName": "Era", "default": True},
                                {"id": 2, "name": "Season of Mastery", "compactName": "SoM", "default": False}],
                 "encounters": [{"id": 1500 + i, "name": n} for i, n in enumerate(self.BOSSES)]},
            ]
        else:
            zones = [
                {"id": 1035, "name": "Temple of Ahn'Qiraj", "frozen": True, "expansion": {"id": 2, "name": "Anniversary"}, "partitions": [], "encounters": []},
                {"id": 1036, "name": "Naxxramas", "frozen": False, "expansion": {"id": 2, "name": "Anniversary"},
                 "partitions": [{"id": 1, "name": "Phase 6", "compactName": "P6", "default": True}],
                 "encounters": [{"id": 1600 + i, "name": n} for i, n in enumerate(self.BOSSES)]},
            ]
        classes = [{"id": cid, "name": cname, "slug": cname, "specs": [{"id": i, "name": sname, "slug": sname} for i, sname in enumerate(specs, 1)]}
                   for cid, (cname, specs) in enumerate(self.CLASSES, 1)]
        return {"zones": zones, "classes": classes, "factions": [{"id": 1, "name": "Alliance"}, {"id": 2, "name": "Horde"}]}

    def _rate(self) -> dict:
        return {"limitPerHour": 3600, "pointsSpentThisHour": self.spent, "pointsResetIn": 2400}

    def _rankings(self, host: str, v: dict) -> dict:
        seed = f"{host}|{v['encounter']}|{v['className']}|{v['specName']}|{v['metric']}|{v['partition']}"
        rng = random.Random(seed)
        n = self.SIZES[rng.randrange(len(self.SIZES))]
        newest = int(self.NEWEST[host].timestamp() * 1000)
        base = {"dps": 900.0, "bossdps": 800.0, "hps": 700.0}[v["metric"]]
        rows = []
        for i in range(n):
            row = {"name": f"Synthetic{i}", "class": v["className"], "spec": v["specName"], "amount": round(max(50.0, rng.gauss(base, base * 0.2)), 1),
                   "duration": int(rng.uniform(90, 300) * 1000), "startTime": newest - int(rng.uniform(0, 100) * 86400 * 1000),
                   "report": {"code": "SYNTHETIC", "fightID": 1, "startTime": newest}, "guild": {"id": 0, "name": "Synthetic", "faction": rng.choice([1, 2])},
                   "server": {"id": 0, "name": "Synthetic", "region": "XX"}, "faction": rng.choice([1, 2])}
            if v.get("combatant"):
                row["talents"] = [{"id": 0, "name": "Synthetic", "points": 0}]
                row["gear"] = [{"id": 0, "name": "Synthetic", "quality": "epic"}]
            rows.append(row)
        rows.sort(key=lambda r: -r["amount"])
        page = v["page"]
        chunk = rows[(page - 1) * 100: page * 100]
        return {"page": page, "hasMorePages": page * 100 < len(rows), "count": len(rows), "rankings": chunk}

    def post(self, url: str, headers: dict, body: bytes, timeout: float = 60.0) -> HttpResponse:
        self.calls += 1
        if url == TOKEN_URL:
            self.token_calls += 1
            if self.token_calls == 1:
                return HttpResponse(500, {}, "synthetic outage")
            return HttpResponse(200, {"content-type": "application/json"}, json.dumps({"token_type": "Bearer", "expires_in": 31536000, "access_token": "synthetic-token"}))
        host = url.split("/")[2]
        req = json.loads(body.decode("utf-8"))
        q = req.get("query", "")
        v = req.get("variables") or {}
        if q.startswith("query RateLimit"):
            return HttpResponse(200, {}, json.dumps({"data": {"rateLimitData": self._rate()}}))
        if q.startswith("query Discovery"):
            self.spent += 1
            z = self._zone_doc(host)
            return HttpResponse(200, {}, json.dumps({"data": {"rateLimitData": self._rate(), "worldData": {"zones": z["zones"]}, "gameData": {"classes": z["classes"], "factions": z["factions"]}}}))
        if q.startswith("query Rankings"):
            self.rankings_calls += 1
            if self.faults:
                f = self.faults.pop(0)
                if f == "401":
                    return HttpResponse(401, {}, "synthetic expired token")
                if f == "429":
                    return HttpResponse(429, {"retry-after": "3"}, "synthetic throttle")
                if f == "500":
                    return HttpResponse(500, {}, "synthetic outage")
                if f == "gql-rate":
                    return HttpResponse(200, {}, json.dumps({"data": {"rateLimitData": self._rate()}, "errors": [{"message": "You are being rate limited (synthetic)"}]}))
            self.spent += 7
            rk = self._rankings(host, v)
            return HttpResponse(200, {}, json.dumps({"data": {"rateLimitData": self._rate(), "worldData": {"encounter": {"id": v["encounter"], "name": "synthetic", "characterRankings": rk}}}}))
        return HttpResponse(400, {}, json.dumps({"errors": [{"message": "unknown synthetic query"}]}))


def dry_run(args, root: Path, paths: dict, log) -> int:
    log("dry run: no network access")
    log("")
    # credentials
    cid, sec, origin = load_credentials(root)
    log(f"credentials: {'found' if cid and sec else 'not found'} (source: {origin}); values are never printed")
    log(f"files/wcl.env git status: {gitignore_status(root, 'files/wcl.env')}")
    log(f"http library: {'requests ' + _requests.__version__ if _requests else 'urllib (requests not installed)'}")
    log("")
    plan = build_plan(args, root)
    log("plan")
    for src in plan["sources"]:
        S = SOURCES[src]
        log(f"  source {src}: {S['label']} on https://{S['host']}/api/v2/client; memo zone {S['memoZoneId']} (verified against worldData.zones at run time); partition: {S['partitionRule']}")
    log(f"  encounters ({len(plan['encounters'])}): " + ", ".join(f"{ENCOUNTERS[k][1]} [{ENCOUNTERS[k][2]}, {ENCOUNTERS[k][3]}]" for k in plan["encounters"]))
    log("  encounter ids: matched by name from worldData.zone.encounters at run time; the memo gives none per boss and none are assumed")
    groups = {}
    for k, (c, s, g) in plan["specs"].items():
        groups.setdefault(g, []).append(f"{c} {s}")
    for g, lst in groups.items():
        log(f"  specs {g} ({len(lst)}): " + ", ".join(lst))
    log(f"  metrics: dps on damage specs, bossdps added on {', '.join(CLEAVE_ENCOUNTERS)}, hps on healers")
    log(f"  percentiles: {', '.join(str(p) for p in PERCENTILES)}; window {plan['windowDays']} days; max pages per cell: {plan['maxPages'] or 'unlimited'}")
    log(f"  cells: {len(plan['cells'])}")
    est_pages = len(plan["cells"]) * 12
    log(f"  page budget: unknown until the pull; at a guessed 12 pages per cell that is ~{est_pages} pages, at {DEFAULT_COST_ESTIMATE:.0f} points per page ~{est_pages * DEFAULT_COST_ESTIMATE / 3600:.1f} free hours")
    log("")
    log("query shapes")
    log("  token: POST " + TOKEN_URL + " with HTTP basic auth (client id and secret) and body grant_type=client_credentials")
    for name, q in (("RateLimit", Q_RATE), ("Discovery", Q_DISCOVERY), ("Rankings", Q_RANKINGS)):
        log(f"  {name} (hash {qhash(q)}):")
        for line in q.splitlines():
            log("    " + line)
    ex = plan["cells"][0] if plan["cells"] else None
    if ex:
        log("  example Rankings variables: " + json.dumps({"encounter": "<id from worldData>", "className": ex["className"], "specName": ex["specName"], "metric": ex["metric"], "partition": "<id from worldData>", "page": 1, "combatant": True}))
    log("")
    log("cache layout")
    for cell in plan["cells"][:3]:
        log(f"  {cell['id']} -> {cache_path(paths, cell, 1).relative_to(root).as_posix()}")
    log(f"  progress: {paths['progress'].relative_to(root).as_posix()}; ids: {paths['ids'].relative_to(root).as_posix()}; log: {paths['log'].relative_to(root).as_posix()}")
    log("  a cached page is reused only when its variables (encounter, class, spec, metric, partition, page) match the current plan")
    log("")
    log("rate limiter check")
    slept = []
    rl = RateLimiter(sleep=lambda s: slept.append(s), log=lambda m: log("  " + m))
    rl.update({"limitPerHour": 3600, "pointsSpentThisHour": 100, "pointsResetIn": 1800}, measure=True)
    rl.update({"limitPerHour": 3600, "pointsSpentThisHour": 112, "pointsResetIn": 1790}, measure=True)
    log(f"  after two responses: {rl.summary()}; wait needed {rl.wait_needed():.0f} s")
    rl.update({"limitPerHour": 3600, "pointsSpentThisHour": 3585, "pointsResetIn": 900})
    log(f"  near the ceiling: {rl.summary()}; wait needed {rl.wait_needed():.0f} s")
    rl.before_request()
    log(f"  before_request slept {slept[-1] if slept else 0:.0f} s (simulated) and reset the counter: {rl.summary()}")
    log("")

    # Everything below runs the real discovery, pull, resume, reduce and render
    # code against an in-memory transport, under files/controls/dry-run/.
    dry_paths = dict(paths)
    dry_paths["controls"] = paths["controls"] / "dry-run"
    dry_paths["raw"] = dry_paths["controls"] / "raw"
    dry_paths["controls_json"] = dry_paths["controls"] / "controls.json"
    dry_paths["controls_md"] = dry_paths["controls"] / "controls.md"
    dry_paths["ids"] = dry_paths["controls"] / "wcl-ids.json"
    dry_paths["progress"] = dry_paths["controls"] / "progress.json"
    if dry_paths["controls"].exists():
        shutil.rmtree(dry_paths["controls"])  # the dry-run tree only; the real cache is never touched here
    subset = dry_run_subset(plan)
    plan_sub = dict(plan, cells=subset)
    fake = FakeTransport(log)
    naps = []
    limiter = RateLimiter(margin_points=args.margin, sleep=lambda s: naps.append(s), log=lambda m: log("  " + m))
    client = WclClient("dry-run-id", "dry-run-secret", limiter, log=lambda m: log("  " + m), sleep=lambda s: naps.append(s), post=fake.post)

    log("transport check: fake endpoints, faults injected (token 500, then 401, 429, 500 and a GraphQL rate-limit error on rankings)")
    log("discovery against the fake worldData")
    ids = run_discovery(client, plan_sub, args, dry_paths, log)
    log("")
    log(f"pull of {len(subset)} cells against the fake endpoints (a mixed slice: both sources, cleave dps and bossdps, a thin spec, a healer)")
    saved_resume, saved_refresh = args.resume, args.refresh
    args.resume, args.refresh = False, False
    run_pull(client, plan_sub, ids, args, dry_paths, log)
    log(f"  transport: {fake.calls} calls, {fake.token_calls} token calls, {fake.rankings_calls} rankings calls; simulated sleeps {', '.join(f'{n:.0f}' for n in naps)} s")
    log("")
    log("resume: second pass over the same cells")
    args.resume = True
    calls_before = fake.calls
    run_pull(client, plan_sub, ids, args, dry_paths, log)
    log(f"  transport calls during resume: {fake.calls - calls_before} (expected 0)")
    args.resume, args.refresh = saved_resume, saved_refresh
    log("")
    log("reduce and render from the dry-run cache")
    ctl = reduce_cells(plan_sub, ids, dry_paths, args, log)
    ctl["synthetic"] = True
    ctl["title"] += " (dry run, synthetic)"
    write_outputs(ctl, plan_sub, dry_paths, log, synthetic=True)
    thin = sum(1 for c in ctl["cells"] if c["thin"])
    log(f"  reduce: {len(ctl['cells'])} cells, {thin} thin, {len(ctl['derived'])} derived; outputs under {dry_paths['controls'].relative_to(root).as_posix()}")
    c0 = next((c for c in ctl["cells"] if c["sampleInWindow"] > 0), None)
    if c0:
        pv = c0["percentiles"]["75"]["provenance"]
        log(f"  provenance on {c0['id']} p75: query {pv['query']} {pv['queryHash']}, partition {pv['partition']}, encounter {pv['encounterId']}, percentile {pv['percentile']}, timestamp {pv['timestamp']}")
    log("")
    log("dry run complete; nothing was sent")
    return 0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def parse_kv(items: list, cast=str) -> dict:
    out = {}
    for it in items or []:
        if "=" not in it:
            raise SystemExit(f"expected source=value, got {it!r}")
        k, v = it.split("=", 1)
        try:
            out[k] = cast(v)
        except ValueError:
            raise SystemExit(f"could not read {v!r} in {it!r}")
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Warcraft Logs control puller (tier one of absolute-numbers.md)")
    ap.add_argument("--dry-run", action="store_true", help="print the plan and query shapes; no network")
    ap.add_argument("--token-check", action="store_true", help="obtain a token and read rateLimitData only")
    ap.add_argument("--discover", action="store_true", help="discovery only; writes files/controls/wcl-ids.json")
    ap.add_argument("--resume", action="store_true", help="reuse wcl-ids.json and skip cells recorded complete")
    ap.add_argument("--reduce-only", action="store_true", help="rebuild controls.json and controls.md from the raw cache")
    ap.add_argument("--refresh", action="store_true", help="ignore the raw cache and refetch")
    ap.add_argument("--root", default=None, help="project root (default: parent of tools/)")
    ap.add_argument("--sources", default="som,anniversary", help="comma list of som,anniversary")
    ap.add_argument("--encounters", default=None, help="comma list of encounter keys (default: all seven)")
    ap.add_argument("--specs", default=None, help="comma list of spec keys or Class/Spec (default: the plan)")
    ap.add_argument("--metrics", default=None, help="restrict to a comma list of dps,bossdps,hps")
    ap.add_argument("--no-thin", action="store_true", help="drop the three thin specs from the plan")
    ap.add_argument("--max-pages", type=int, default=0, help="cap pages per cell (0 = all)")
    ap.add_argument("--window-days", type=int, default=DEFAULT_WINDOW_DAYS)
    ap.add_argument("--window-end", action="append", default=[], metavar="SRC=YYYY-MM-DD", help="explicit window end per source")
    ap.add_argument("--zone", action="append", default=[], metavar="SRC=ID", help="zone id override per source")
    ap.add_argument("--partition", action="append", default=[], metavar="SRC=ID", help="partition id override per source")
    ap.add_argument("--host", action="append", default=[], metavar="SRC=HOST", help="host override per source")
    ap.add_argument("--margin", type=float, default=0.0, help="extra points to keep in reserve under the hourly limit")
    args = ap.parse_args(argv)

    args.window_end = parse_kv(args.window_end)
    for k, v in args.window_end.items():
        try:
            parse_date(v)
        except ValueError:
            raise SystemExit(f"--window-end {k}={v}: expected YYYY-MM-DD")
    args.zone_override = parse_kv(args.zone, int)
    args.partition_override = parse_kv(args.partition, int)
    args.host_override = parse_kv(args.host)

    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parent.parent
    controls = root / "files" / "controls"
    paths = {
        "root": root, "controls": controls, "raw": controls / "raw",
        "controls_json": controls / "controls.json", "controls_md": controls / "controls.md",
        "ids": controls / "wcl-ids.json", "progress": controls / "progress.json", "log": controls / "pull.log",
    }
    log = Log(None if args.dry_run else paths["log"])

    if args.dry_run:
        return dry_run(args, root, paths, log)

    plan = build_plan(args, root)

    if args.reduce_only:
        ids = read_json(paths["ids"])
        if not ids:
            log(f"no {paths['ids']}; run discovery first")
            return 2
        missing = [s for s in plan["sources"] if s not in ids.get("sources", {})]
        if missing:
            log(f"wcl-ids.json lacks {', '.join(missing)}; rerun discovery or narrow --sources")
            return 2
        ctl = reduce_cells(plan, ids, paths, args, log)
        write_outputs(ctl, plan, paths, log)
        return 0

    cid, sec, origin = load_credentials(root)
    if not (cid and sec):
        log("no credentials: set WCL_CLIENT_ID and WCL_CLIENT_SECRET in the environment or in files/wcl.env")
        return 2
    log(f"credentials loaded from {origin}")
    limiter = RateLimiter(margin_points=args.margin, log=log)
    client = WclClient(cid, sec, limiter, log=log)

    try:
        client.token()
        if args.token_check:
            for src in plan["sources"]:
                host = args.host_override.get(src, SOURCES[src]["host"])
                body = client.graphql(host, Q_RATE)
                rl = (body.get("data") or {}).get("rateLimitData") or {}
                log(f"  {host}: limit {rl.get('limitPerHour')} points/hour, spent {rl.get('pointsSpentThisHour')}, reset in {rl.get('pointsResetIn')} s")
            log("token check complete")
            return 0

        ids = read_json(paths["ids"]) if args.resume else None
        if ids:
            missing = [s for s in plan["sources"] if s not in ids.get("sources", {})]
            if missing:
                log(f"wcl-ids.json lacks {', '.join(missing)}; rerunning discovery")
                ids = None
            else:
                log(f"resume: using {paths['ids']} discovered {ids.get('discoveredAt')}")
        if ids is None:
            ids = run_discovery(client, plan, args, paths, log)
        if args.discover:
            return 0
        run_pull(client, plan, ids, args, paths, log)
        ctl = reduce_cells(plan, ids, paths, args, log)
        write_outputs(ctl, plan, paths, log)
        log(f"done: {client.requests_made} requests this run; {limiter.summary()}")
        return 0
    except FatalError as e:
        log(f"fatal: {e}")
        return 1
    except KeyboardInterrupt:
        log("interrupted; rerun with --resume")
        return 130


if __name__ == "__main__":
    sys.exit(main())
