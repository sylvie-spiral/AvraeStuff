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
  druid = load_json(get("subclass", "{}")).get("DruidLevel", "").lower()
  if druid == "shepherd":
    # continue
    if DruidLevel >=10:
      ms.append(f"**{name}** uses the Guardian Spirit subclass feature")
      ms.append("")
      ms.append("Beginning at 10th level, your Spirit Totem safeguards the beasts and fey that you call forth with your magic. When a beast or fey that you summoned or created with a spell ends its turn in your Spirit Totem aura, that creature regains a number of hit points equal to half your druid level.")
      ms.append("")

      its = []
      nope =[]

      heal = int(DruidLevel / 2)
      ms.append(f"Healing each creature for {heal} hp.")

      # find the group
      g = combat().get_group(grp)
      if g == None:
        ms.append(f"""Could not find a {grp} group - did you use !conjure?""")
      else:
        for i in g.combatants:
          if i.creature_type:
            ltype = i.creature_type.lower()
            if "fey" in ltype or "beast" in ltype:
              ef = i.get_effect("Spirit Totem Aura:")
              if not ef:
                nope.append(f"{i.name} (No Aura)")
              if i.hp <= 0:
                nope.append(f"{i.name} (Dead)")
              else:
                i.damage(f"-{heal}[healing]")
                its.append(f"{i.name} ({i.hp}/{i.max_hp})")
            else:
              nope.append(f"{i.name} ({i.creature_type})")
          else:
            nope.append(f"{i.name} (no creature type)")

      ms.append("")
      
      if len(its):
        ms.append("**Applied to**:")
        ms.append(", ".join(its))
      else:
        ms.append("Make sure you have used the appropriate !totem commands.")

      ms.append("**Not applied to**:")
      if len(nope):
        ms.append(", ".join(nope))
      else:
        ms.append("All creatures were effected.")
      
    else:
      ms.append("Requires level 10.")
  else:
    ms.append("Rquires Shepherd (did you !level druid shepherd?")
else:
  ms.append("Avrae doesn't track your creatures out of combat, so get your pencil and write it down.")
      
dt = "\n".join(ms)
o.append(f"""!embed -desc "{dt}" -footer "!guardianSpirit" """)
return "\n".join(o)
</drac2>