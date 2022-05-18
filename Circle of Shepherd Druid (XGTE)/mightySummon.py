multiline
<drac2>
o = []
ms = []

ch = character()

pa = argparse("&*&")
ar = [x.lower() for x in &ARGS&]

grp = f"""CO-{name}"""
aSP = load_json(get_gvar("9e91a358-654e-45cc-b7bd-94365858e88c"))

#is there an initiative?
if combat():
  # are we a Circle of Shepherd druid (!level Druid Shepherd)
  druid = sClass=load_json(get("subclass", "{}")).get("DruidLevel", "").lower()
  if druid == "shepherd":
    # continue
    if DruidLevel >=6:      
      ms.append(f"**{name}** is a *Mighty Summoner*")
      ms.append("Starting at 6th level, beasts and fey that you conjure are more resilient than normal. Any beast or fey summoned or created by a spell that you cast gains the following benefits:")
      ms.append("* The creature appears with more hit points than normal: 2 extra hit points per Hit Die it has.")
      ms.append("* The damage from its natural weapons is considered magical for the purpose of overcoming immunity and resistance to nonmagical attacks and damage.")
      ms.append("")

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

        its = []
        nope = []

        if cr == None:
          ms.append(f"""Couldn't find {w} in database, if it's a beast/fey conjure, contact Technomancers to add it.""")
        else:
          gain = (2 * cr.HD)
          hp = cr.HP + gain

          for i in g.combatants:
            i.set_maxhp(hp)
            i.set_hp(hp)
  
          ms.append(f"""Each {w} gains {gain} hp.""")

        for i in g.combatants:          
          if i.creature_type:
            ltype = i.creature_type.lower()
            if "beast" in ltype or "fey" in ltype:
              i.add_effect("Mighty Summoner", "-magical")
              its.append(f"{i.name}")
          else:
            nope.append(f"{i.name} ({i.creature_type})")

        ms.append("")
        
        if len(its):
          ms.append("**Applied to**:")
          ms.append(", ".join(its))

        if len(nope):
          ms.append("**Not applied to**:")
          ms.append(", ".join(nope))

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