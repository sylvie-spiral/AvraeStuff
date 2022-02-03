multiline
<drac2>
o = []
ms = []

ch = character()

pa = argparse("&*&")
ar = &ARGS&

grp = f"""CO-{name}"""
aSP = load_json(get_gvar("9e91a358-654e-45cc-b7bd-94365858e88c"))

#is there an initiative?
if combat():
  # are we a Circle of Shepherd druid (!level Druid Shepherd)
  druid = sClass=load_json(get("subclass", "{}")).get("DruidLevel", "").lower()
  if druid == "shepherd":
    # continue
    if ch.levels.get("Druid") >=6:
      # find the group
      g = combat().get_group(grp)
      if g == None:
        ms.append(f"""Could not find a {grp} group - did you use !conjure?""")
      else:
        # find the creature in the dictionaries
        w = g.combatants[0].monster_name

        gvars = []
        for x in aSP:
          sp = aSP.get(x)
          if sp.shep:
            for v in sp.gvar:
              if not v in gvars:
                gvars.append(v)

        cr = None
        for x in gvars:
          ratings = load_json(get_gvar(x))

          for r in ratings:
            rat = ratings.get(r)
            for c in rat:
              # this will always be an exact match
              if w == c:
                cr = rat.get(c)
                break
            if cr:
              break

        # classfeat spam
        o.append("!classfeat \"Mighty Summoner\"")

        if cr == None:
          ms.append(f"""Couldn't find {w} in database, if it's a conjure, contact Technomancers to add it.""")
        else:
          gain = (2 * cr.HD)
          hp = cr.HP + gain

          for i in g.combatants:
            i.set_maxhp(hp)
            i.set_hp(hp)
  
          ms.append(f"""Mighty summoner added {gain} hp to each {w}.""")

        for i in g.combatants:
          if i.creature_type and i.creature_type.lower() in ["beast","fey"]:            
            i.add_effect("Mighty Summoner", "-magical", desc = "Mighty Summoner - summoned creatures attacks are magical.")
          else:
            ms.append(f"""Creature '{i.name}' in '{grp}' is {i.creature_type} - but this feat wants fey or beast.""")

        ms.append(f"""Set attacks on the {grp} group to magical.""")

    else:
      ms.append(f"""You need to be at least level 6 to use this ability. Do you need to !update?""")
  else:
    ms.append(f"""This command only works for Circle of Shepherd, do you need to !level druid shepherd?""")
else:
  ms.append(f"""Apply this in combat after using !conjure to create the {grp} group.""")

dt = "\n".join(ms)
o.append(f"""!embed -desc "{dt}" -footer "!mightySummon (use in initiative after conjure) | @SylvieTG#4737" """)

return "\n".join(o)
</drac2>