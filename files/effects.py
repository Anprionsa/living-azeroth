#!/usr/bin/env python3
"""Propose structured effects from talent text.

Validated against warrior-arms-rebuilt, which is hand-authored ground truth.
Output is marked source:proposed and must be reviewed before it counts as data.
"""
import json, re, sys
P="/mnt/user-data/outputs/talent-data.json"
D=json.load(open(P))
ABIL={}
for a in D["abilities"]: ABIL.setdefault(a["class"],{})[a["name"].lower()]=a["id"]
TAGS={"fire","frost","arcane","shadow","holy","nature","physical","bleed","poison","curse","disease",
      "periodic","melee","ranged","spell","heal","absorb","threat","pet","totem","trap","stealth","weapon","form"}

def scope(sent, cls):
    s=sent.lower()
    for nm,aid in sorted(ABIL.get(cls,{}).items(), key=lambda kv:-len(kv[0])):
        if re.search(r"\b"+re.escape(nm)+r"\b", s): return {"ability":aid}
    for t in sorted(TAGS,key=len,reverse=True):
        if re.search(r"\byour "+t+r"s?\b|\b"+t+r" (spells?|damage|attacks?|effects?)\b", s): return {"tag":t}
    return {"all":True}

def cond(sent):
    s=sent.lower()
    for pat,fn in [(r"below (\d+)% (?:target )?health", lambda m:f"target.health<{int(m.group(1))/100}"),
                   (r"above (\d+)% health", lambda m:f"target.health>{int(m.group(1))/100}"),
                   (r"critical(?:ly)?\b", lambda m:"event.critical"),
                   (r"\bon a dodge\b|\bdodged\b", lambda m:"event.dodged"),
                   (r"\bon a parry\b|\bparried\b", lambda m:"event.parried"),
                   (r"\bon a block\b|\bblocking\b", lambda m:"event.blocked"),
                   (r"\bat full stacks?\b", lambda m:"self.stacks==max"),
                   (r"\bkilling blow\b|\bkills? its target\b|\bon death\b|\bwhen .* dies\b", lambda m:"event.targetDeath"),
                   (r"\balready bleeding\b|\bbleeding target\b", lambda m:"target.bleeding"),
                   (r"\bwhile (?:you are )?stunned\b", lambda m:"self.stunned")]:
        m=re.search(pat,s)
        if m: return fn(m)
    return None

# every rule may fire; a sentence can yield several effects
RULES=[
 (r"\bignores? (armou?r|resistance)\b", lambda m,s,c:{"op":"ignore","stat":"armor" if "arm" in m.group(1) else "resistance","magnitude":1.0}),
 (r"cannot be (dodged|parried|resisted|dispelled|interrupted|reflected|avoided|cleansed|overhealed)\b",
   lambda m,s,c:{"op":"enable","flag":"immune_"+{"overhealed":"overheal","avoided":"missed","cleansed":"dispelled","critically struck":"crit","disarmed":"disarm"}.get(m.group(1),m.group(1)),"magnitude":1.0}),
 (r"\bcannot be (disarmed|feared|slowed|rooted|critically struck)\b",
   lambda m,s,c:{"op":"enable","flag":"immune_"+{"overhealed":"overheal","avoided":"missed","cleansed":"dispelled","critically struck":"crit","disarmed":"disarm"}.get(m.group(1),m.group(1)).replace(" ","_"),"magnitude":1.0}),
 (r"may be (cast|used) (?:while |in )(moving|stunned|silenced|casting|combat|any stance|defensive stance)\b",
   lambda m,s,c:{"op":"enable","flag":"use_"+{"any stance":"any_stance","defensive stance":"any_stance"}.get(m.group(2),m.group(2)),"magnitude":1.0}),
 (r"\busable in combat\b", lambda m,s,c:{"op":"enable","flag":"use_combat","magnitude":1.0}),
 (r"\bin any stance\b", lambda m,s,c:{"op":"enable","flag":"use_any_stance","magnitude":1.0}),
 (r"\bcosts? no (mana|rage|energy|focus|shard)\b", lambda m,s,c:{"op":"multiply","stat":"cost","magnitude":0.0}),
 (r"\bgrants? (?:you )?(?:an? )?(?:additional )?combo point", lambda m,s,c:{"op":"add","stat":"comboPoint","magnitude":None}),
 (r"\bfree\b(?!.*\bnot\b)", lambda m,s,c:{"op":"multiply","stat":"cost","magnitude":0.0}),
 (r"\brefunds? (its |their |the )?(rage|energy|mana|cooldown)", lambda m,s,c:{"op":"add","stat":{"combo point":"comboPoint","soul shard":"soulShard"}.get(m.group(2),m.group(2)),"magnitude":None}),
 (r"\brefreshe?s\b|\bextends?\b", lambda m,s,c:{"op":"refresh","stat":"duration","magnitude":None}),
 (r"\bdoes not (expire|decay|fall off)\b|\bpersists?\b|\bno longer expires?\b", lambda m,s,c:{"op":"enable","flag":"no_expiry","magnitude":1.0}),
 (r"\bcooldown (?:is )?resets?\b|\bresets? (?:the )?cooldown\b|\bresets? \w+\b", lambda m,s,c:{"op":"refresh","stat":"cooldown","magnitude":None}),
 (r"\btwice as fast\b", lambda m,s,c:{"op":"multiply","stat":"tickRate","magnitude":2.0}),
 (r"\bdouble[sd]?\b", lambda m,s,c:{"op":"multiply","stat":"effect","magnitude":2.0}),
 (r"\bcounts? as (?:a |an )?(\w+)\b", lambda m,s,c:({"op":"convert","addTags":[m.group(1)],"magnitude":None} if m.group(1) in TAGS else None)),
 (r"\b(?:a |an )?(?:second|additional|nearby|extra) (?:target|enemy|ally|opponent)\b", lambda m,s,c:{"op":"addTarget","magnitude":1.0}),
 (r"\bspreads? to\b|\bchains? to\b|\bjumps? to\b", lambda m,s,c:{"op":"addTarget","magnitude":1.0}),
 (r"\bby (\d+)%", lambda m,s,c:{"op":"multiply","stat":"effect","magnitude":1+int(m.group(1))/100}),
 (r"\bgrants? (?:you )?(?:an? )?(?:additional )?(rage|energy|stack)", lambda m,s,c:{"op":"add","stat":{"combo point":"comboPoint","soul shard":"soulShard"}.get(m.group(1),m.group(1)),"magnitude":None}),
 (r"\bgenerates? (Rage|rage|energy|threat|mana)\b", lambda m,s,c:{"op":"add","stat":m.group(1).lower(),"magnitude":None}),
 (r"\bhas a chance to\b|\bmay (stun|root|interrupt|silence)\b|\bchance to (stun|root)\b",
   lambda m,s,c:{"op":"proc","stat":(m.group(1) or m.group(2) or "damage"),"magnitude":None}),
 (r"\bheals? you\b|\brestores? (?:your )?health\b", lambda m,s,c:{"op":"add","stat":"selfHeal","magnitude":None}),
 (r"\bcause[sd]? (?:the (?:opponent|target) to )?bleed\w*\b", lambda m,s,c:{"op":"proc","stat":"bleed","magnitude":None}),
 (r"\bstrike an additional\b", lambda m,s,c:{"op":"addTarget","magnitude":1.0}),
]

def parse(text, cls):
    out=[]
    for sent in re.split(r"(?<=\.)\s+", text):
        if len(sent.split())<3: continue
        sc, cn = scope(sent, cls), cond(sent)
        seen=set()
        for pat,fn in RULES:
            m=re.search(pat, sent, re.I)
            if not m: continue
            e=fn(m,sent,cls)
            if not e: continue
            k=(e["op"], e.get("stat") or e.get("flag") or "")
            if k in seen: continue
            seen.add(k)
            e["scope"]=sc
            if cn: e["when"]=cn
            e["source"]="proposed"
            out.append(e)
    return out

if __name__=="__main__":
    # validate against the hand-authored reference before touching anything
    ref=next(t for t in D["trees"] if t["id"]=="warrior-arms-rebuilt")
    tp=fn_=0
    for r in ref["rows"]:
        for x in r["talents"]:
            got=parse(x["text"], ref["class"])
            want=[e for e in x["effects"] if e.get("source")=="authored"]
            gk={(e["op"], e.get("stat") or e.get("flag") or "") for e in got}
            wk={(e["op"], e.get("stat") or e.get("flag") or "") for e in want}
            tp+=len(gk&wk); fn_+=len(wk-gk)
    print(f"against the Arms reference: {tp} effects matched, {fn_} missed, recall {100*tp//(tp+fn_)}%")
    if "--apply" in sys.argv:
        n=0
        for t in D["trees"]:
            if t["kind"]=="vanilla" or t["id"]=="warrior-arms-rebuilt": continue
            for r in t["rows"]:
                for x in r["talents"]:
                    if any(e.get("source")=="authored" for e in x.get("effects",[])): continue
                    e=parse(x["text"], t["class"])
                    if e: x["effects"]=e; n+=1
        json.dump(D,open(P,"w"),indent=1,ensure_ascii=False)
        print(f"applied to {n} talents")
