import json, re
O="/mnt/user-data/outputs/"
VOCAB={"fire","frost","arcane","shadow","holy","nature","physical","bleed","poison","curse","disease",
 "periodic","melee","ranged","spell","heal","absorb","threat","shout","pet","totem","trap","weapon",
 "stealth","form"}
def slug(s): return re.sub(r"[^a-z0-9]+","-",s.lower()).strip("-")

trees=[]
# 1. vanilla
V=json.load(open(O+"talents-classified.json"))["classes"]
for cls,tt in V.items():
    for tree,ts in tt.items():
        rows={}
        for n,x in ts.items():
            g=x["reqPoints"]
            rows.setdefault(g,[]).append({"id":slug(cls+"-"+tree+"-"+n),"name":n,"ranks":x["maxRank"],
              "text":re.sub(r"\$\{\[.*?\]\}","N",x["description"]),
              "buys":"number" if x["buys"]=="flat" else ("ability" if x.get("candidateActive") else "behavior"),
              "reads":[],"modifies":[],"grants":[],"crossTree":None,"flags":[]})
        trees.append({"id":slug(cls+"-"+tree),"class":cls,"name":f"{cls} {tree}","kind":"vanilla",
          "status":"shipped","supersedes":None,"mechanic":None,
          "dividend":{"stats":[],"thresholds":[],"calibratedAgainst":None},"lore":None,
          "rows":[{"row":g//5+1,"gate":g,"talents":rows[g]} for g in sorted(rows)]})
# 2. rebuilt
R=json.load(open(O+"rebuilt-trees.json"))
for t in R["trees"]:
    cls=t["class"]
    rows=[]
    for r in t["rows"]:
        tal=[]
        for x in r["talents"]:
            fl=[]
            tx=x["text"]
            if re.search(r"subtraction",tx,re.I): fl.append("subtraction")
            if r["points"]==20 and re.search(r"the mark",tx,re.I): fl.append("mark")
            if r["points"]>=30: fl.append("capstone")
            if re.search(r"aura",x["name"]+tx,re.I): fl.append("aura")
            ct=None
            if re.search(r"cross-tree|sideways",tx,re.I):
                ct={"target":None,"standsAlone":bool(re.search(r"stands alone|every \w+ has",tx,re.I))}
            tal.append({"id":slug(t["name"]+"-"+x["name"]),"name":x["name"],"ranks":x["ranks"],"text":tx,
              "buys":"number" if re.match(r"^(Increases|Reduces|Decreases)\b",tx) else "behavior",
              "reads":[c for c in x.get("reads",[]) if c in VOCAB],"modifies":[],"grants":[],
              "crossTree":ct,"flags":fl})
        rows.append({"row":r["row"],"gate":r["points"],"talents":tal})
    trees.append({"id":slug(t["name"])+"-rebuilt","class":cls,"name":t["name"],"kind":"rebuilt",
      "status":"committed","supersedes":slug(t["name"]),"mechanic":None,
      "dividend":{"stats":[],"thresholds":[],"calibratedAgainst":None},"lore":None,"rows":rows})
# 3. absorbed and original
A=json.load(open(O+"trees.json"))
for t in A["trees"]:
    rows=[]
    for r in t["rows"]:
        tal=[]
        for x in r["talents"]:
            tx=x["text"]; fl=[]
            if re.search(r"subtraction",tx,re.I): fl.append("subtraction")
            if re.search(r"the mark",tx,re.I): fl.append("mark")
            if r["points"]>=30: fl.append("capstone")
            if re.search(r"aura",x["name"]+tx,re.I): fl.append("aura")
            ct={"target":None,"standsAlone":bool(re.search(r"stands alone|every \w+ has",tx,re.I))} \
               if re.search(r"cross-tree",tx,re.I) else None
            tal.append({"id":slug(t["name"]+"-"+x["name"]),"name":x["name"],"ranks":x.get("ranks",1),
              "text":tx,"buys":"number" if re.match(r"^(Increases|Reduces|Decreases)\b",tx) else "behavior",
              "reads":[],"modifies":[],"grants":[],"crossTree":ct,"flags":fl})
        rows.append({"row":r["row"],"gate":r.get("points",5*(r["row"]-1)),"talents":tal})
    trees.append({"id":t["id"],"class":t["host"],"name":t["name"],
      "kind":"original" if t.get("source")=="original" else "absorbed",
      "status":t.get("status","committed"),"supersedes":None,
      "mechanic":{"name":t["localMechanic"].split(",")[0],"description":t["localMechanic"]},
      "dividend":{"stats":[],"thresholds":[],"calibratedAgainst":"local mechanic scaling, per REG-C1"},
      "lore":{k:t.get(k) for k in ("verb","verbNote","professionGate","permanentCost","worldAnchors","loreAnchor")},
      "rows":rows})

for t in trees:
    t["availablePoints"]=sum(x["ranks"] for r in t["rows"] for x in r["talents"])
out={"meta":{"schema":"1.0","date":"2026-08","vocabulary":sorted(VOCAB),
  "counts":{k:sum(1 for t in trees if t["kind"]==k) for k in ("vanilla","rebuilt","absorbed","original")},
  "note":"See SCHEMA.md. Abilities table is intentionally empty; it is the gear socket."},
  "abilities":[], "trees":trees}
json.dump(out,open(O+"talent-data.json","w"),indent=1,ensure_ascii=False)
print("talent-data.json written")
print(" ",out["meta"]["counts"],"| total trees:",len(trees),
      "| talents:",sum(len(r["talents"]) for t in trees for r in t["rows"]))
