#!/usr/bin/env python3
"""Vanilla combat model simulator reading talent-data.json.

Implements the documented level-60-versus-level-63 model: single-roll attack table,
glancing blows on white only, armor mitigation, vanilla rage generation, 200% melee
crits and 150% spell crits. Absolute output is still approximate; the comparison is
relative and every modelled term is one that does NOT cancel between two builds.
"""
import json, random, statistics
D=json.load(open("/mnt/user-data/outputs/talent-data.json"))
ABIL={a["id"]:a for a in D["abilities"]}
TREES={t["id"]:t for t in D["trees"]}
TALENT_GRANTED=({e["scope"]["ability"] for t in D["trees"] for r in t["rows"] for x in r["talents"]
                 for e in x.get("effects",[]) if e["op"]=="grant" and e.get("scope",{}).get("ability")}
                | {g for t in D["trees"] for r in t["rows"] for x in r["talents"] for g in x.get("grants",[])})

# level 60 attacker, level 63 boss, 315 defense, 300 weapon skill
BOSS={"level":63,"defense":315,"armor":3731}
PET_BASE=0.45   # a pet swing as a fraction of a player swing
PET_CAP=2       # simultaneous pets, before talents that raise it
BASE_MISS=0.08; BASE_DODGE=0.056; GLANCE=0.40
_d=BOSS["defense"]-300
GLANCE_MULT=((1.3-0.05*_d)+(1.2-0.03*_d))/2      # 0.65 at 300 skill, a 35% reduction
SPELL_MISS=0.17                                   # vs +3 level, capped by 16% hit
ARMOR_DR=BOSS["armor"]/(BOSS["armor"]+400+85*60)  # standard level-60 mitigation

# Naxxramas-tier stat blocks, one per class, held constant. Absolute values are
# approximate; they cancel between two builds of the same class, which is the point.
# gear blocks live in the data so they can be calibrated against logged output
GEAR=D.get("gear") or {}

CASTER={"Mage","Warlock","Priest"}

DPS_STATS={"damage","effect","critChance","tickRate","cost","cooldown","castTime",
           "openingDamage","frontload","comboPoint","attackSpeed","rage","energy","movingDamage","cleaveEvery","poisonStacks","poisonStack"}
TANK_STATS={"threat","armor","dodge","parry","blockChance","blockValue","health","damageTaken","defense"}
HEAL_STATS={"healing","cost","critChance","mana","manaPool","castTime"}
def _value(x, role="dps", castable=None):
    """Approximate what a player optimising output would pick.

    Counts downside as well as upside. A subtraction node that zeroes a damage school is
    not worth five points because it has effects; the selector took Backdraft on a
    Shadow Bolt rotation and dropped the build from 399 to 43 damage per second.
    """
    v=0
    for e in x.get("effects",[]):
        if e.get("source")!="authored": continue
        m=e.get("magnitude"); st=e.get("stat"); sc=e.get("scope",{})
        # an effect scoped to an ability the build never casts is worth nothing, unless
        # the talent is what grants that ability in the first place
        _ab=sc.get("ability")
        if castable is not None and _ab and _ab not in castable and e["op"]!="grant" \
           and _ab not in x.get("grants",[]): continue
        if e["op"]=="enable" and e.get("flag") in ("poison_instant","poison_from_finisher"): v+=6
        if role=="tank":
            # a tank values threat and survival, and pays for them with damage
            if e["op"]=="enable" and e.get("flag")=="immune_crit": v+=40; continue
            if st in TANK_STATS:
                if e["op"]=="multiply" and st=="damageTaken" and m is not None: v+= 30*(1.0-m); continue
                if e["op"]=="multiply" and st=="threat" and m is not None: v+= 30*(m-1.0); continue
                if e["op"]=="add" and m is not None: v+= 12*abs(m) if st in ("dodge","parry","blockChance") else 6; continue
            if e["op"]=="multiply" and st in ("damage","critChance") and m is not None and m<1.0: continue
        elif role=="heal":
            if e["op"]=="multiply" and st=="healing" and m is not None: v+= 30*(m-1.0); continue
            if e["op"]=="multiply" and st=="cost" and m is not None: v+= 20*(1.0-m); continue
            if e["op"]=="multiply" and st in ("damage",) and m is not None: continue
        broad = bool(sc.get("all") or sc.get("tag"))     # a whole school versus one ability
        if e["op"]=="grant": v+=10
        elif e["op"]=="multiply" and st in ("damage","effect","healing","critChance"):
            if m is None: v+=1
            elif m<=0.01: v-= 40 if broad else 10        # zeroing a school is catastrophic
            elif m<1.0:   v-= (30 if broad else 10)*(1.0-m)
            else:         v+= min(12, (30 if broad else 12)*(m-1.0))
        elif e["op"]=="multiply" and st in ("cost","cooldown","castTime"):
            v += min(8, 12*(1.0-(m if m is not None else 1.0)))
        elif e["op"]=="add" and st in DPS_STATS: v+=5
        elif e["op"] in ("proc","addTarget","ignore"): v+=3
        else: v+=1
    if "subtraction" in x.get("flags",[]) and v<8: v-=10
    return v

def build(tid, pts, cfg="core", forceCapstone=False, role="dps", castable=None):
    """Greedy by value under gate constraints, which is how players actually build.

    Filling low rows to completion before moving up is not player behaviour and made
    a 30-point build miss a gate-15 talent a 31-point build reached. Here each point
    goes to the best rank currently legal, and cheap filler is bought only to open a
    gate that a better talent sits behind.
    """
    t=TREES[tid]; rows=sorted(t["rows"], key=lambda r:r["gate"])
    avail=[x for r in rows for x in r["talents"]
           if not (x.get("availableIn") and cfg not in x["availableIn"])]
    val=lambda x:_value(x, role, castable)
    gate={x["name"]: r["gate"] for r in rows for x in r["talents"]}
    taken={}; ranks={n:0 for n in gate}; spent=0
    reserve=0
    if forceCapstone:
        caprow=max(rows, key=lambda r:r["gate"])
        cap=[x for x in caprow["talents"] if not (x.get("availableIn") and cfg not in x["availableIn"])]
        if cap and pts>=caprow["gate"]+1:
            reserve=1; capTalent=cap[0]
        else: forceCapstone=False
    while spent < pts-reserve:
        legal=[x for x in avail if ranks[x["name"]]<x["ranks"] and gate[x["name"]]<=spent]
        if not legal: break
        best=max(legal, key=lambda x:(val(x), gate[x["name"]], x["name"]))
        if val(best)<=0:
            # nothing valued is available. If a higher gate exists, buy filler nearest it.
            # If none does, still spend the point: a capstone with no authored effects is
            # not worthless, it is unmeasured, and refusing to buy it silently shortens the build.
            nxt=min((g for g in {gate[x["name"]] for x in avail} if g>spent), default=None)
            if nxt is not None:
                best=max(legal, key=lambda x:(-gate[x["name"]], x["name"]))
        ranks[best["name"]]+=1; spent+=1; taken[best["name"]]=(best, ranks[best["name"]])
    if forceCapstone and reserve:
        ranks[capTalent["name"]]+=1; spent+=1; taken[capTalent["name"]]=(capTalent,1)
    return taken, spent

def treeDepthScalar(splits):
    """The depth dividend for the tree a build is deepest in."""
    if not splits: return 1.0
    tid=max(splits, key=lambda z:z[1])[0]
    t=TREES.get(tid) or {}
    return float(t.get("depthCoefficient", 1.0))

def treeDepthScalar(splits):
    """The depth dividend for the tree a build is deepest in. One scalar per tree, which
    is the protocol's lever for band neutrality: it moves a spec's output without editing
    a single talent."""
    if not splits: return 1.0
    tid=max(splits, key=lambda z:z[1])[0]
    return float((TREES.get(tid) or {}).get("depthCoefficient", 1.0))

def modifiers(taken):
    m={"cost":{}, "cooldown":{}, "critChance":{}, "damage":{}, "extraTargets":{},
       "flags":set(), "procs":[], "granted":set(), "debuff":{}, "consume":{}, "alternate":[],
       "damage_pet_add":{}, "opening":{}, "frontload":{}, "castTime":{},
       "refresh":set(), "noExpiry":set(), "range":{}, "comboAdd":{}, "control":{},
       "convert":{}, "uptime":0.0, "interruptGuard":0.0, "dispelGuard":0.0,
       "cleaveEvery":0, "cleaveTargets":1, "moving":{},
       "poisonMaxStacks":0, "poisonInstant":False, "poisonFromFinisher":False, "poisonSpend":0.0,
       "damageAdd":{}, "critDamage":{}}
    for val in taken.values():
        x, ranks = val if isinstance(val,tuple) else (val, val["ranks"])
        frac = ranks/max(1,x["ranks"])
        for g in x.get("grants",[]):
            if ranks>0: m["granted"].add(g)
        for e in x.get("effects",[]):
            if e.get("source")!="authored": continue
            sc=e.get("scope",{}); key=sc.get("ability") or sc.get("tag") or "all"; v=e.get("magnitude")
            if v is not None and e["op"]=="multiply": v = 1.0 + (v-1.0)*frac
            elif v is not None and e["op"] in ("add","proc","ignore"): v = v*frac
            op,st=e["op"], e.get("stat")
            if op=="multiply" and st=="cost" and v is not None: m["cost"][key]=m["cost"].get(key,1.0)*v
            elif op=="multiply" and st=="cooldown" and v is not None: m["cooldown"][key]=m["cooldown"].get(key,1.0)*v
            elif op=="multiply" and st=="castTime" and v is not None: m["castTime"][key]=m["castTime"].get(key,1.0)*v
            elif op=="multiply" and st in ("damage","effect") and v is not None:
                if e.get("when")=="event.critical":
                    m["critDamage"][key]=m["critDamage"].get(key,1.0)+(v-1.0)
                else:
                    m["damage"][key]=m["damage"].get(key,1.0)+(v-1.0)
            elif op=="add" and st=="damage" and key=="pet" and v is not None:
                m["damage_pet_add"]["pet"]=m["damage_pet_add"].get("pet",0.0)+v
            elif op=="add" and st=="critChance" and v is not None: m["critChance"][key]=m["critChance"].get(key,0.0)+v
            elif op=="addTarget": m["extraTargets"][key]=m["extraTargets"].get(key,0)+int(v or 1)
            elif op=="enable" and e.get("flag")=="poison_instant":
                m["poisonInstant"]=True; m["flags"].add(e.get("flag"))
            elif op=="enable" and e.get("flag")=="poison_from_finisher":
                m["poisonFromFinisher"]=True; m["flags"].add(e.get("flag"))
            elif op=="add" and st=="damage" and v is not None:
                # a general additive damage bonus. Previously only the pet tag had one,
                # so every other add/damage effect fell through the chain and did nothing.
                m["damageAdd"][key]=m["damageAdd"].get(key,0.0)+v
            elif op=="enable": m["flags"].add(e.get("flag"))
            elif op=="grant" and sc.get("ability"): m["granted"].add(sc["ability"])
            elif op=="proc" and v is not None: m["procs"].append((key, st, v))
            elif op=="debuff" and v is not None:
                # a stacking vulnerability: worth its magnitude times its stack count, ramped
                m["debuff"][key]=m["debuff"].get(key,0.0)+v*min(4,e.get("stacks",1))
            elif op=="consume" and v is not None:
                # spends a stack for burst: worth its magnitude on the consuming ability
                m["consume"][key]=m["consume"].get(key,0.0)+v
            elif op=="add" and st=="openingDamage" and v is not None:
                m["opening"][key]=m["opening"].get(key,0.0)+v
                m["opening"]["_window"]=max(m["opening"].get("_window",0.0), e.get("window",15.0))
            elif op=="add" and st=="frontload" and v is not None:
                m["frontload"][key]=m["frontload"].get(key,0.0)+v
            elif op=="add" and st=="poisonStacks" and v is not None:
                m["poisonMaxStacks"]+=v
            elif op=="enable" and e.get("flag")=="poison_instant": m["poisonInstant"]=True
            elif op=="enable" and e.get("flag")=="poison_from_finisher": m["poisonFromFinisher"]=True
            elif op=="consume" and st=="poisonStack" and v is not None: m["poisonSpend"]+=v
            elif op=="add" and st=="movingDamage" and v is not None:
                m["moving"][key]=m["moving"].get(key,0.0)+v
            elif op=="add" and st=="cleaveEvery" and v is not None:
                m["cleaveEvery"]=int(v)
                m["cleaveTargets"]=max(m["cleaveTargets"], int(e.get("extraTargets",1)))
            elif op=="convert":
                # a conversion adds tags, so an ability inherits the modifiers of the
                # school it now counts as. Unarmed counting as a weapon, a weapon as frost.
                for tg in e.get("addTags",[]): m["convert"].setdefault(key,set()).add(tg)
            elif op=="enable" and e.get("flag")=="immune_interrupted":
                # an uninterruptible cast is one that never has to be started again
                m["interruptGuard"]=min(0.06, m["interruptGuard"]+0.02)
            elif op=="enable" and e.get("flag") in ("immune_dispelled","no_decay"):
                # a periodic that cannot be removed or decay keeps its full duration
                m["dispelGuard"]=min(0.05, m["dispelGuard"]+0.015)
            elif op=="enable" and e.get("flag") in ("use_any_angle","use_combat","use_casting",
                    "use_any_stance","use_stealth","no_gcd","no_positional","weapon_fork","break_control",
                    "immune_feared","immune_stunned","immune_disarm","carry_forward","use_stunned"):
                # each of these removes a condition that would otherwise cost casts. Modelled
                # as uptime rather than as damage, since that is what they actually buy.
                m["uptime"]+= 0.012 if e["op"]=="enable" else 0.0
            elif op=="add" and st=="healingReduction" and v is not None:
                m["control"]["all"]=m["control"].get("all",0.0)+v*0.10
            elif op=="add" and st=="absorb" and v is not None:
                m["control"]["all"]=m["control"].get("all",0.0)+v*0.05
            elif op=="refresh" and st in ("duration","cooldown"):
                m["refresh"].add((st,key))
            elif op=="enable" and e.get("flag")=="no_expiry": m["noExpiry"].add(key)
            elif op=="add" and st=="comboPoint" and v is not None:
                m["comboAdd"][key]=m["comboAdd"].get(key,0.0)+v
            elif op=="add" and st=="range" and v is not None: m["range"][key]=m["range"].get(key,0.0)+v
            elif op=="proc" and st in ("stun","root","silence","interrupt") and v is not None:
                # crowd control on a boss does nothing, but the uptime it buys against
                # adds is real. Counted as a small throughput credit rather than ignored.
                m["control"][key]=m["control"].get(key,0.0)+v*0.04
            elif op=="proc" and st in ("bleed","sunder","extra_attack") and v is not None:
                m["procs"].append((key, st, v))
            elif op=="alternate" and v is not None:
                m["alternate"].append((e.get("pair",[]), v))
    return m

def lookup_add(mods, key, aid):
    """Additive lookup for behaviour effects, which stack rather than compound."""
    m=mods.get(key,{}); v=m.get(aid,0.0)
    for tg in ABIL.get(aid,{}).get("tags",[]): v+=m.get(tg,0.0)
    return v+m.get("all",0.0)

def lookup(mods, key, aid, default):
    """Ability id first, then each of the ability's tags, then all. Tag-scoped effects
    were previously collected and never applied, which silenced most authored effects."""
    m=mods[key]
    if aid in m: return m[aid]
    v=None
    for tg in ABIL.get(aid,{}).get("tags",[]):
        if tg not in m: continue
        if key=="damage": v=(v if v is not None else 1.0)+(m[tg]-1.0)
        elif key in ("cost","cooldown"): v=(v if v is not None else default)*m[tg]
        else: v=(v or 0)+m[tg]
    if v is not None: return v
    return m.get("all", default)

def white_swing(g, mods, rng):
    """Single-roll table: miss, dodge, glancing, crit, hit. Parry and block are zero from behind."""
    miss=max(0.0, BASE_MISS-g["hit"]); dodge=BASE_DODGE
    crit=min(g["critChance"]+mods["critChance"].get("all",0.0), max(0.0, 1-miss-dodge-GLANCE))
    r=rng.random()
    if r<miss: return 0.0,"miss"
    r-=miss
    if r<dodge: return 0.0,"dodge"
    r-=dodge
    if r<GLANCE: return GLANCE_MULT,"glance"
    r-=GLANCE
    if r<crit: return 2.0,"crit"
    return 1.0,"hit"

def yellow_hit(g, mods, aid, rng):
    """Yellow attacks do not glance."""
    miss=max(0.0, BASE_MISS-g["hit"]); dodge=BASE_DODGE
    fl=mods.get("flags",set())
    tg=ABIL.get(aid,{}).get("tags",[])
    if "immune_missed" in fl: miss=0.0
    if "immune_dodged" in fl or "immune_parried" in fl: dodge=0.0
    crit=g["critChance"]+lookup(mods,"critChance",aid,0.0)
    r=rng.random()
    if r<miss: return 0.0,"miss"
    r-=miss
    if r<dodge: return 0.0,"dodge"
    r-=dodge
    if r<crit: return 2.0,"crit"
    return 1.0,"hit"

def spell_hit(g, mods, aid, rng):
    miss=max(0.01, SPELL_MISS-g["hit"])
    if "immune_resisted" in mods.get("flags",set()): miss=0.01
    crit=g["critChance"]+lookup(mods,"critChance",aid,0.0)+mods.get("_cdCrit",0.0)
    r=rng.random()
    if r<miss: return 0.0,"resist"
    r-=miss
    if r<crit: return 1.5,"crit"          # vanilla spell crits are 150%, not 200%
    return 1.0,"hit"

CD=D.get("cooldowns",{})
SC=D.get("scenarios",{})
def run(cls, splits, seconds=None, seed=1, targets=None, scenario="patchwerk"):
    sc=SC.get(scenario, {})
    seconds = seconds if seconds is not None else sc.get("seconds",300)
    targets = targets if targets is not None else sc.get("targets",1)
    move = sc.get("movementFraction",0.0)
    switch = sc.get("targetSwitchEvery")
    rng=random.Random(seed)
    g=GEAR[cls]; taken={}
    # what the class can actually cast, so the selector does not buy improvements to
    # abilities this build never uses
    _cast=set()
    for _k in ("priority","healingPriority","feralPriority"):
        for _e in D["rotations"].get(cls,{}).get(_k,[]) or []:
            _cast.add(_e["ability"] if isinstance(_e,dict) else _e)
    _deepest = max(range(len(splits)), key=lambda i: splits[i][1]) if splits else 0
    for i,(tid,pts) in enumerate(splits):
        taken.update(build(tid, pts, forceCapstone=(i==_deepest and pts>=31), castable=_cast)[0])
    mods=modifiers(taken)
    _R=D["rotations"][cls]
    _deep = max(splits, key=lambda z: z[1])[0] if splits else ""
    _key="priority"
    if "feralPriority" in _R and ("feral" in _deep or _deep in ("druid-feral-combat-rebuilt",)): _key="feralPriority"
    elif "healingPriority" in _R and any(k in _deep for k in ("restoration","holy","discipline","chronomancer","radiance","dreamer")):
        _key="healingPriority"
    rot=[e if isinstance(e,dict) else {"ability":e} for e in _R.get(_key) or _R["priority"]]
    # a build always keeps its class's maintained and granted abilities regardless of list
    if _key!="priority":
        _have={e["ability"] if isinstance(e,dict) else e for e in rot}
        for e in _R["priority"]:
            a0=e["ability"] if isinstance(e,dict) else e
            if a0 in TALENT_GRANTED and a0 not in _have: rot.append(e if isinstance(e,dict) else {"ability":a0})
    # how tight is mana? Compare what an uninterrupted rotation would spend against what
    # the pool plus regeneration supplies over the fight.
    _pool=g.get("manaPool",0.0); _regen=g.get("mp5",0.0)/5.0*seconds
    _costs=[ (ABIL[e["ability"]].get("cost") or 0) for e in rot
             if e["ability"] in ABIL and ABIL[e["ability"]].get("costType")=="mana"]
    _avg=sum(_costs)/len(_costs) if _costs else 0
    _need=_avg*(seconds/1.8) if _avg else 0
    _manaTight=0.0 if not _need else max(0.0, min(0.85, 1.0-(_pool+_regen)/_need))
    _avgCost=_avg
    _dpmScale=1.0
    # the tree's DOMINANT school, not every school it mentions. Mage Fire references frost
    # through Frostfire and Fire and Ice, so counting any mention made both schools its own
    # and a Fire build still cast Frostbolt.
    _school=set()
    if splits:
        _dt=next((t for t in D["trees"] if t["id"]==max(splits, key=lambda z: z[1])[0]), None)
        if _dt:
            _cnt={}
            for _r in _dt["rows"]:
                for _x in _r["talents"]:
                    for _e in _x.get("effects",[]):
                        _tg=_e.get("scope",{}).get("tag")
                        if _tg in ("fire","frost","arcane","shadow","holy","nature","melee","ranged","poison","bleed","weapon"):
                            _cnt[_tg]=_cnt.get(_tg,0)+1
                        _ab=_e.get("scope",{}).get("ability")
                        if _ab:
                            for _t2 in ABIL.get(_ab,{}).get("tags",[]):
                                if _t2 in ("fire","frost","arcane","shadow","holy","nature","melee","ranged","poison","bleed","weapon"):
                                    _cnt[_t2]=_cnt.get(_t2,0)+1
            if _cnt:
                _top=max(_cnt.values())
                _school={k for k,v in _cnt.items() if v>=_top*0.75}
    def _worth(ent):
        a=ABIL.get(ent["ability"])
        if not a: return -1
        d=(a.get("baseDamage") or 0)
        d+= g.get("spellDamage",0)*(a.get("spCoefficient") or 0)
        d+= g.get("attackPower",0)*((a.get("apCoefficient") or 0)+(a.get("rapCoefficient") or 0))
        hits=min(targets, a.get("maxTargets", 1) if a.get("maxTargets") else (targets if a.get("minTargets") else 1))
        tm=max(a.get("castTime") or 0.0, a.get("gcd") if a.get("gcd") is not None else 1.5, 0.5)
        dps=d*max(1,hits)/tm
        # a spec casts its own school. Applied to the final value rather than to the
        # throughput half, or the mana blend dilutes it and a Fire build casts Frostbolt.
        _sb = 1.30 if (_school and set(a.get("tags",[])) & _school) else 1.0
        # blend throughput with efficiency in proportion to how constrained the resource
        # is over the fight. A class that can cast freely ignores cost; one that cannot
        # ranks by damage per point spent, which is what a player does.
        rt=a.get("costType"); c=a.get("cost") or 0
        if rt=="mana" and c>0 and _manaTight>0:
            dpm=d*max(1,hits)/c
            return (dps*(1-_manaTight) + dpm*_manaTight*_dpmScale)*_sb
        return dps*_sb
    _keep=[e for e in rot if e.get("maintain") or not ABIL.get(e["ability"],{}).get("baseDamage")]
    _fillers=[e for e in rot if e not in _keep]
    if _fillers and _manaTight>0:
        _ref=max(_worth(e) for e in _fillers) or 1.0
        _dpmScale=_ref/max(1e-6, max((ABIL[e["ability"]].get("baseDamage") or 1)/max(1,(ABIL[e["ability"]].get("cost") or 1)) for e in _fillers))
    _fill=sorted(_fillers, key=lambda e:-_worth(e))
    rot=_keep+_fill
    physical = cls not in CASTER and "attackPower" in g
    pool={"rage":0.0, "energy":100.0, "mana":g.get("manaPool",7500.0)}
    t=0.0; gcd=0.0; cd={}; total=0.0; casts={}; swing=0.0; aura={}; dots={}; cp=0; last_cast=None
    selfBuff={}   # active maintenance buffs on the player, keyed by stat
    queued=None   # an on-next-swing ability waiting for the swing timer
    strikeCount=0 # for periodic cleave effects
    poison=0.0    # stacks held on the target
    poisonTick=0.0
    pets=[]       # active pets, each an expiry time. Pets attack on their own timer and
                  # were previously summoned and then ignored entirely.
    petSwing=0.0
    # a pet is summoned before the pull. Charging the summon to the fight cost a pet class
    # both a global cooldown and the pet's opening seconds.
    for ent0 in rot:
        a0=ABIL.get(ent0["ability"])
        if a0 and a0.get("prePull") and "pet" in a0.get("tags",[]):
            if ent0["ability"] in TALENT_GRANTED and ent0["ability"] not in mods["granted"]: continue
            cap0=min(PET_CAP+2, 1+int(lookup_add(mods,"extraTargets","pet")))
            for _ in range(a0.get("summons",1)):
                if len(pets)<cap0: pets.append(a0["duration"])
            # a summon paid for before the pull must not be paid for again during it
            aura[ent0["ability"]]=a0["duration"]
            if a0.get("cooldown"): cd[ent0["ability"]]=a0["cooldown"]
    overpower_ready=0.0
    EXEC={"warrior-execute","warlock-shadowburn","paladin-hammer-of-wrath"}
    mycd={k:v for k,v in CD.items() if v["class"]==cls and k in mods["granted"]}
    cdReady={k:0.0 for k in mycd}; cdActive={}
    while t<seconds:
        # a maintenance buff on attack speed shortens the swing timer, which is most of
        # what Slice and Dice is worth
        _as=selfBuff.get("attackSpeed",(0.0,0.0))
        _hs=(1.0+_as[0]) if _as[1]>t else 1.0
        # ranged auto attack, the hunter equivalent of a white swing
        _ranged=ABIL.get(cls.lower()+"-auto-shot") or ABIL.get("hunter-auto-shot")
        if cls=="Hunter" and _ranged is not None and t>=swing:
            mult,kind=yellow_hit(g,mods,_ranged["id"],rng)
            rd=((_ranged.get("baseDamage") or 0)+g.get("attackPower",0)*(_ranged.get("apCoefficient") or 0.20))*mult
            rd*= mods["damage"].get("ranged",1.0)*(1-ARMOR_DR)
            total+=rd
            if mult>0: casts["Auto Shot"]=casts.get("Auto Shot",0)+1
            swing=t+(_ranged.get("shotSpeed",3.0))/_hs
        elif physical and t>=swing:
            mult,kind=white_swing(g,mods,rng)
            wd=(g["weaponDamage"]*g["weaponSpeed"] + g["attackPower"]/14*g["weaponSpeed"])*mult
            # talent damage multipliers apply to white damage too. Without this a melee tree's
            # multipliers touch only its specials, and for a class whose damage is mostly
            # autoattack that is nearly the whole tree doing nothing.
            wd*= mods["damage"].get("melee", 1.0) * mods["damage"].get("physical", 1.0)
            wd*= 1.0 + (selfBuff.get("armorReduction",(0,0))[0] if selfBuff.get("armorReduction",(0,0))[1]>t else 0)
            for k in cdActive:
                if "damage" in mycd[k]["effect"]: wd*=mycd[k]["effect"]["damage"]
            wd*=(1-ARMOR_DR)
            if queued and mult>0:
                qa=ABIL[queued]
                bonus=(qa.get("baseDamage") or 0)+g.get("attackPower",0)*(qa.get("apCoefficient") or 0)
                bonus*=mods["damage"].get("melee",1.0)*mult*(1-ARMOR_DR)
                wd=bonus                              # it replaces the swing, not adds to it
                casts[qa["name"]]=casts.get(qa["name"],0)+1
            queued=None
            total+=wd
            if kind=="dodge": overpower_ready=t+5.0
            if cls=="Rogue" and mult>0 and ABIL.get("rogue-deadly-poison"):
                _pa2=ABIL["rogue-deadly-poison"]
                if rng.random()<_pa2.get("applyChance",0.3):
                    poison=min(_pa2.get("maxStacks",5)+round(mods["poisonMaxStacks"]), poison+1)
            if "paladin-seal-of-command" in mods["granted"] and mult>0 and rng.random()<0.07*g["weaponSpeed"]/3.5:
                total += (g["weaponDamage"]*g["weaponSpeed"]*0.7)*(1-ARMOR_DR)
            pool["rage"]=min(100.0, pool["rage"] + (wd/230.6*7.5 if wd>0 else 2.0))
            swing=t+g["weaponSpeed"]/_hs
        # fire any granted cooldown that is off cooldown
        for k,v in mycd.items():
            if t>=cdReady[k] and k not in cdActive:
                cdActive[k]=t+v["duration"]; cdReady[k]=t+v["cooldown"]
        for k,exp in list(cdActive.items()):
            if t>exp: del cdActive[k]
        mods["_cdCrit"]=sum(mycd[k]["effect"].get("critChance",0.0) for k in cdActive)
        # movement windows block hard casts
        moving = move>0 and (int(t/10.0)%10) < int(move*10)
        if switch and t>0 and int(t)%switch==0 and abs(t-int(t))<0.05:
            dots.clear(); aura.clear()
        for ent in rot:
            aid=ent["ability"]; a=ABIL.get(aid)
            if not a or (a.get("baseDamage") is None and "pet" not in a.get("tags",[])): continue
            if t<cd.get(aid,0) or t<gcd: continue
            if aid in TALENT_GRANTED and aid not in mods["granted"]: continue
            if a.get("onNextSwing"):
                # queue it against the swing timer; it costs rage and no global cooldown
                if queued or not physical: continue
                c2=(a.get("cost") or 0)*lookup(mods,"cost",aid,1.0)
                if c2>pool.get("rage",0.0): continue
                pool["rage"]-=c2; queued=aid
                continue
            if aid in EXEC and (t/seconds)<0.8: continue
            # do not apply a periodic that cannot tick out. Nobody refreshes an eighteen
            # second effect with five seconds left, and modelling it that way makes every
            # tree built on periodics look weak in short fights for the wrong reason.
            dur=a.get("duration") or (ent.get("duration") if ent.get("maintain") else 0)
            if dur and a.get("tickInterval") and (seconds-t) < dur*0.5: continue
            if "pet" in a.get("tags",[]) and dur and (seconds-t) < 5: continue
            if a.get("prePull") and t < 1.0: continue
            # an area ability below its target threshold is a damage loss, and a
            # conditional ability fires only under its condition
            if a.get("minTargets") and targets < a["minTargets"]: continue
            if a.get("condition")=="never": continue
            if a.get("condition")=="event.dodged" and t>overpower_ready: continue
            if moving and (a.get("castTime") or 0)>0 and "use_moving" not in mods["flags"]: continue
            if aid=="warrior-overpower" and t>overpower_ready: continue
            if ent.get("maintain") and t < aura.get(aid,0)-1.5: continue
            if "pet" in a.get("tags",[]) and t < aura.get(aid,0): continue
            if a.get("finisher") and cp<5: continue
            cost=(a.get("cost") or 0)*lookup(mods,"cost",aid,1.0)
            rt=a.get("costType") or "mana"
            if cost>pool.get(rt,0.0): continue
            if rt=="mana" and _manaTight>0 and cost>_avgCost and pool["mana"] < g.get("manaPool",1)*0.30:
                # a caster low on mana stops casting its expensive spells and falls back
                # to efficient ones. Spending the pool freely and then idling is not what
                # anyone does, and it made removing a cast time a loss.
                continue
            dmg=a.get("baseDamage") or 0
            if a.get("finisher"): dmg*=cp/5.0
            if a.get("apCoefficient"): dmg+=g.get("attackPower",0)*a["apCoefficient"]
            if a.get("rapCoefficient"): dmg+=g.get("attackPower",0)*a["rapCoefficient"]
            if a.get("spCoefficient"): dmg+=g.get("spellDamage",0)*a["spCoefficient"]
            dmg*=lookup(mods,"damage",aid,1.0)
            for _k in ("armorReduction","rangedDamage","missChance"):
                _b=selfBuff.get(_k)
                if _b and _b[1]>t: dmg*=1.0+_b[0]
            # behaviour effects: a vulnerability ramps, a consumed stack pays out, and an
            # alternation pays only when you actually alternate
            dmg*=1.0+lookup_add(mods,"debuff",aid)
            dmg*=1.0+lookup_add(mods,"consume",aid)
            dmg*=1.0+lookup_add(mods,"control",aid)
            dmg*=1.0+lookup_add(mods,"damageAdd",aid)
            dmg*=1.0+mods["uptime"]+mods["interruptGuard"]
            if a.get("duration") and a.get("tickInterval"): dmg*=1.0+mods["dispelGuard"]
            for tg in set(mods["convert"].get(aid,set())) | set(mods["convert"].get("all",set())):
                dmg*= mods["damage"].get(tg,1.0)
            # a bleed or extra attack proc is real damage on top of the strike
            for pk,pst,pv in mods["procs"]:
                if pk!=aid and pk not in a.get("tags",[]) and pk!="all": continue
                if pst=="extra_attack" and rng.random()<pv: dmg*=1.6
                elif pst in ("bleed","sunder") and rng.random()<pv: dmg*=1.15
            # an opening window pays only in the first seconds of a fight, so it is worth
            # a third of a forty-five second fight and a twentieth of a five minute one
            # a lever that only pays while moving narrows a movement hole without
            # touching any other scenario
            if moving and mods["moving"]: dmg*=1.0+lookup_add(mods,"moving",aid)
            if mods["opening"] and t < mods["opening"].get("_window",15.0):
                dmg*=1.0+lookup_add(mods,"opening",aid)
            for pair,v in mods["alternate"]:
                if aid in pair and last_cast is not None and last_cast in pair and last_cast!=aid:
                    dmg*=1.0+v
            for k in cdActive:
                e=mycd[k]["effect"]
                if "damage" in e: dmg*=e["damage"]
            if physical:
                mult,kind=yellow_hit(g,mods,aid,rng); dmg*=mult*(1-ARMOR_DR)
            else:
                mult,kind=spell_hit(g,mods,aid,rng); dmg*=mult
            if kind=="crit":
                _cd=lookup(mods,"critDamage",aid,1.0)
                if _cd!=1.0: dmg*=_cd
            strikeCount+=1
            tg=1+min(mods["extraTargets"].get(aid,0), targets-1)
            if mods["cleaveEvery"] and strikeCount % mods["cleaveEvery"]==0:
                tg+= min(mods["cleaveTargets"], max(0,targets-tg))
            # an area ability hits everything present up to its own cap. The priority
            # ranked it as if it did and the damage did not, so a rotation switching to
            # AoE on cleave was switching to single-target damage on a slower cast.
            if a.get("minTargets"):
                tg=max(tg, min(targets, a.get("maxTargets") or targets))
            elif a.get("maxTargets"): tg=min(tg*targets, a["maxTargets"])
            total+=dmg*tg
            casts[a["name"]]=casts.get(a["name"],0)+1
            pool[rt]=pool.get(rt,0.0)-cost
            if "pet" in a.get("tags",[]) and (a.get("duration") or 0)>0:
                cap=min(PET_CAP+2, 1+int(lookup_add(mods,"extraTargets","pet")))
                for _ in range(a.get("summons",1)):
                    if len(pets)<cap: pets.append(t+a["duration"])
            if a.get("finisher"):
                if mods["poisonFromFinisher"] and cls=="Rogue":
                    poison=min(ABIL["rogue-deadly-poison"].get("maxStacks",5)+round(mods["poisonMaxStacks"]), poison+1)
                if mods["poisonSpend"]>0 and poison>0:
                    dmg*= 1.0+mods["poisonSpend"]*poison; poison=max(0,poison-2)
                cp=0
            elif a.get("comboPoints"):
                extra=lookup_add(mods,"comboAdd",aid)
                cp=min(5, cp+a["comboPoints"]+int(extra))
                if extra%1 and rng.random()<(extra%1): cp=min(5,cp+1)
            if ent.get("maintain"):
                aura[aid]=t+ent.get("duration",a.get("duration") or 15)
                for k,v in (a.get("grantsSelf") or {}).items(): selfBuff[k]=(v, aura[aid])
                for k,v in (a.get("grantsTarget") or {}).items(): selfBuff[k]=(v, aura[aid])
            if a.get("duration") and a.get("tickInterval"):
                ticks=max(1,int(a["duration"]/a["tickInterval"]))
                fl=lookup_add(mods,"frontload",aid)
                if fl>0:
                    # a front-loaded periodic pays part of its total on application, which
                    # is worth most when the fight may end before it ticks out
                    total-=dmg*tg*(1.0-fl)
                    dots[aid]=(t+a["duration"], a["tickInterval"], dmg*tg*(1.0-fl)/ticks, t)
                else:
                    dots[aid]=(t+a["duration"], a["tickInterval"], dmg*tg/ticks, t)
                    total-=dmg*tg
            cd[aid]=t+(a.get("cooldown") or 0)*lookup(mods,"cooldown",aid,1.0)
            _ct=(a.get("castTime") or 0.0)*lookup(mods,"castTime",aid,1.0)
            if a.get("channel"): _ct=max(_ct, a.get("duration") or _ct)
            for k in cdActive: _ct/= mycd[k]["effect"].get("haste",1.0)
            gcd=t+max(_ct, a.get("gcd") if a.get("gcd") is not None else 1.5)
            last_cast=aid
            break
        # poison. Stacks build on weapon swings and the damage is proportional to what is
        # held, so a talent that changes the ramp changes real output.
        _pa=ABIL.get("rogue-deadly-poison") if cls=="Rogue" else None
        if _pa is not None:
            cap=_pa.get("maxStacks",5)+round(mods["poisonMaxStacks"])
            if mods["poisonInstant"] and poison<cap and t>swing-g.get("weaponSpeed",2.7): poison=cap
            if t>=poisonTick and poison>0:
                per=((_pa.get("baseDamage") or 0)+g.get("attackPower",0)*(_pa.get("apCoefficient") or 0))*poison
                per*= lookup(mods,"damage","rogue-deadly-poison",1.0)
                per*= 1.0+lookup_add(mods,"debuff","rogue-deadly-poison")
                per*= 1.0+lookup_add(mods,"damageAdd","rogue-deadly-poison")
                total+= per*(1-ARMOR_DR*0.0)
                casts["Deadly Poison"]=casts.get("Deadly Poison",0)+1
                poisonTick=t+_pa.get("tickInterval",3)

        # pet damage. A pet swings on its own timer and is unaffected by the player's
        # global cooldown, which is most of what a pet class is.
        pets=[e for e in pets if e>t]
        if pets and t>=petSwing:
            # a vanilla pet contributes real but modest damage. The base is deliberately
            # small because a tree's pet talents are what should make it matter, and a
            # large hardcoded base is a number no tuner can reach.
            _own = g.get("attackPower") or g.get("spellDamage",600)*2.2
            base=(_own/14*2.0 + 40)*PET_BASE
            base*= 1.0 + lookup_add(mods,"damage_pet_add", "pet")
            base*= mods["damage"].get("pet",1.0)
            total += base*min(len(pets), PET_CAP+2)*(1-ARMOR_DR)
            petSwing=t+2.0
        for aid,(exp,iv,per,last) in list(dots.items()):
            if aid in mods["noExpiry"] or any(k==aid for _,k in mods["refresh"]) or \
               any(k in ABIL.get(aid,{}).get("tags",[]) for _,k in mods["refresh"]):
                exp=max(exp, t+iv)          # kept alive by refreshes or by never expiring
                dots[aid]=(exp,iv,per,last)
            if t<=exp and t-last>=iv:
                total+=per; dots[aid]=(exp,iv,per,t)
            elif t>exp: del dots[aid]
        t+=0.1
        _rr=1.0
        for k in cdActive: _rr*= mycd[k]["effect"].get("resourceRate",1.0)
        pool["energy"]=min(100.0, pool["energy"]+0.1*10.0*_rr)                # 20 energy per 2 sec
        pool["mana"]=min(g.get("manaPool",7500.0), pool["mana"]+0.1*g.get("mp5",300)/5.0*_rr)
    return total*treeDepthScalar(splits)/seconds, casts, len(taken)

def compare(cls, tests, targets=1, seeds=20):
    out=[]
    for label,sp in tests:
        runs=[run(cls,sp,seed=s,targets=targets)[0] for s in range(1,seeds+1)]
        out.append((label, statistics.mean(runs), statistics.pstdev(runs)))
    return out

if __name__=="__main__":
    W=[("Arms 31 / Fury 20",[("warrior-arms-rebuilt",31),("warrior-fury-rebuilt",20)]),
       ("Arms 30 / Fury 21",[("warrior-arms-rebuilt",30),("warrior-fury-rebuilt",21)]),
       ("Fury 31 / Arms 20",[("warrior-fury-rebuilt",31),("warrior-arms-rebuilt",20)]),
       ("Fury 30 / Arms 21",[("warrior-fury-rebuilt",30),("warrior-arms-rebuilt",21)])]
    for tg in (1,3):
        print(f"\n=== Warrior, {tg} target{'s' if tg>1 else ''}")
        base=None
        for label,m,sd in compare("Warrior",W,targets=tg):
            if base is None: base=m
            print(f"  {label:22} {m:7.0f} dps  sd {sd:4.1f}   {100*(m-base)/base:+6.1f}%")
