#!/usr/bin/env python3
"""Three independent controls, so the claim rests on more than two free tests.

CLASSIC   Warcraft Tavern Phase 6 Naxxramas, Anniversary realms, Jan 2026. Median parse.
WOWTBC    wowtbc.gg Phase 6 Naxxramas, top 10% parses. A DIFFERENT SITE, DIFFERENT
          PERCENTILE, same game. Tests whether the sim tracks the ladder or one dataset.
SOD       Warcraft Tavern Phase 7 Naxxramas, Season of Discovery. Twenty-one specs, and
          the runes changed every class while the reworked trees did not, so agreement
          here would be meaningless and DISagreement is the expected result.
"""
CLASSIC={  # median parse, twelve specs
 "Warrior DPS":1411,"Rogue DPS":1151,"Mage Fire":1019,"Warlock DPS":887,
 "Hunter Marksmanship":856,"Druid Feral":839,"Shaman Enhancement":687,
 "Shaman Elemental":675,"Priest Shadow":596,"Paladin Retribution":524,
 "Druid Balance":503,"Mage Frost":446}

WOWTBC={   # top 10% parses, a separate site and percentile
 "Warrior DPS":1274,"Rogue DPS":1105,"Mage Fire":987,"Warlock DPS":841,
 "Druid Feral":783,"Hunter Marksmanship":776,"Shaman Elemental":711,
 "Mage Frost":678,"Shaman Enhancement":622,"Priest Shadow":542,
 "Paladin Retribution":522,"Druid Balance":501}

SOD={      # Season of Discovery phase 7, runes active
 "Mage Fire":22277,"Druid Balance":22080,"Druid Feral":21712,"Warlock DPS":21445,
 "Paladin Retribution":21259,"Hunter Marksmanship":20790,"Rogue DPS":20663,
 "Shaman Elemental":20523,"Priest Shadow":20376,"Warrior DPS":20018,
 "Mage Frost":19900,"Shaman Enhancement":19328}

def share(d):
    top=max(d.values())
    return {k:100.0*v/top for k,v in d.items()}
