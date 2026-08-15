import re, json
T = open("/mnt/user-data/outputs/classic-plus-talent-design.md", encoding="utf-8").read()
body = T[T.index("## 6. Worked example"):T.index("## 20. The absorbed trees")]

FULL = {"6":"Warrior Arms","7":"Hunter Marksmanship","8":"Shaman Enhancement","9":"Warlock Demonology",
 "10":"Druid Feral Combat","11":"Paladin Retribution","12":"Paladin Protection","13":"Priest Discipline",
 "14":"Shaman Elemental","15":"Priest Holy","16":"Druid Balance"}
BATCH = {"17.1":"Hunter Beast Mastery","17.2":"Hunter Survival","17.3":"Shaman Restoration",
 "17.4":"Warlock Affliction","17.5":"Warrior Fury","18.1":"Paladin Holy","18.2":"Rogue Combat",
 "18.3":"Mage Frost","18.4":"Rogue Assassination","19.1":"Mage Arcane","19.2":"Druid Restoration",
 "19.3":"Priest Shadow"}

TAL = re.compile(r"\*([A-Z][^*\n]{2,42}?)\*\s*\((\d+)\)")
DEL = re.compile(r"delet|merged into|folded into|returned as dividend|absorbed into", re.I)
CUT = re.compile(r"(?m)^[A-Z][\w' ]{2,44}(?:,? and [A-Z][\w' ]{2,44})* (?:is|are) delet")

def talents(text):
    c = CUT.search(text)
    if c: text = text[:c.start()]
    out = []
    for m in TAL.finditer(text):
        if DEL.search(text[m.end():m.end()+42]):
            continue
        name = m.group(1).strip().rstrip('.,:').strip()
        tail = text[m.end():]
        desc = re.split(r"(?=\*[A-Z][^*\n]{2,42}?\*\s*\()", tail)[0]
        desc = re.sub(r"\s+", " ", re.sub(r"^[.,:\s]+", "", desc)).strip()
        out.append({"name": name, "ranks": int(m.group(2)), "text": desc[:280]})
    return out

trees = {}
for s in re.split(r"\n(?=## \d+\. )", body):
    mnum = re.match(r"## (\d+)\.", s.split("\n")[0])
    if not mnum: continue
    n = mnum.group(1)
    if n in FULL:
        rows = {}
        for b in re.split(r"\n(?=\*\*(?:Gate|Tier|Row) \d+)", s):
            g = re.match(r"\*\*(?:Gate|Tier) (\d+)", b) or re.match(r"\*\*Row \d+ \((\d+) points", b)
            if not g: continue
            rows.setdefault(int(g.group(1)), []).extend(talents(b.split("\n\n**")[0]))
        if rows: trees[FULL[n]] = rows
    else:
        for sub in re.split(r"\n(?=### \d+\.\d+ )", s):
            sh = re.match(r"### (\d+\.\d+) ", sub)
            if not sh or sh.group(1) not in BATCH: continue
            rows = {}
            for gm in re.finditer(r"^- \*\*(?:Gate|Row \d+, gate) (\d+), (\d+)[^*]*\*\*(.*)$", sub, re.M):
                rows.setdefault(int(gm.group(1)), []).extend(talents(gm.group(3)))
            if rows: trees[BATCH[sh.group(1)]] = rows

STATED = {"Warrior Arms":50,"Hunter Marksmanship":52,"Shaman Enhancement":50,"Warlock Demonology":50,
 "Druid Feral Combat":55,"Paladin Retribution":52,"Paladin Protection":50,"Priest Discipline":52,
 "Shaman Elemental":50,"Priest Holy":52,"Druid Balance":52,"Hunter Beast Mastery":48,
 "Hunter Survival":52,"Shaman Restoration":56,"Warlock Affliction":49,"Warrior Fury":60,
 "Paladin Holy":52,"Rogue Combat":62,"Mage Frost":52,"Rogue Assassination":52,"Mage Arcane":52,
 "Druid Restoration":55,"Priest Shadow":52}
print(f"{'tree':24} {'pts':>4} {'stated':>7} {'diff':>5}")
for n in sorted(trees):
    pts = sum(t["ranks"] for v in trees[n].values() for t in v)
    st = STATED.get(n); d = pts-st if st else None
    flag = "" if d in (0,None) else "  <<<"
    print(f"  {n:24} {pts:4} {str(st or '-'):>7} {str(d if d is not None else '-'):>5}{flag}")
print(f"\nextracted {len(trees)} of 27")
json.dump(trees, open("rebuilt-raw.json","w"), indent=1)
