  elif parsedArgs.last("heal"):
    if not combat():
      # finish off
      out.append(f"""There should be an active combat at this point.""")
    else:

        group = combat().get_group(groupname, True)
        if not group:
            out.append(f"""-heal should only execute after the original !i madd from running the alias normally.""")
        else:
            numHP = parsedArgs.last("heal", 0, int)

            for (critter) in group.combatants:
                numToHeal = numHP

                if critter.hp < critter.max_hp:
                    maxHeal = critter.max_hp - critter.hp
                    if (numToHeal > maxHeal):
                        numToHeal = maxHeal
                else:
                    numToHeal = 0

                out.append(f"""!echo {critter.name} - {numToHeal}""")
                
                if (numToHeal > 0):
                    out.append(f"""!i hp "{critter.name}" {numToHeal} """)

<drac2>
    out = []
    groupname = f"""CO-{name}"""
    out.append(f"""{groupname}""")

    if not combat():
      # finish off
      out.append(f"""There should be an active combat at this point.""")

    # locate the group
    group = combat().get_group(groupname, True)
    if not group:
      out.append(f"""-finish should only execute after the original !i madd from running the alias normally.""")

    else:
        # find the first critter
        critter = group.combatants[0]
        creature = f""" "{critter.monster_name}" """

        CR = critter.levels.total_level
        if (CR < 0.25):
            CR = 0.25

        # number to summon:
        numSummon = int(2 / CR) - 1

        if (numSummon > 0):
            addCmd = f"""!i madd {creature} {commonPart} -n {numSummon} """
            out.append(addCmd)

    return "\n".join(out)
</drac2>
<drac2>
    out = []
    groupname = f"""CO-{name}"""
    out.append(f"""!echo add the HPs""")

    if not combat():
      # finish off
      out.append(f"""There should be an active combat at this point.""")
    else:        
        # locate the group
        group = combat().get_group(groupname, True)
        if not group:
            out.append(f"""-buff should only execute after the original !i madd from running the alias normally.""")
        else:
            numHP = group.combatants[0].max_hp + parsedArgs.last("buff", 0, int)

            messages = []
            messages.append(f"""{ch.name} applies a max hp / temp hp to some critters.""")

            # add the HP to all creatures
            for (critter) in group.combatants:
                critter.set_maxhp(numHP)
                critter.set_hp(numHP)   

                messages.append(f"""{critter.monster_name} ({critter.name}) ({critter.hp}/{critter.max_hp})""")
            
            msg = "\n".join(messages)
            out.append(f"""!embed -desc "{msg}" """)
</drac2>

<drac2>
    out = []
    groupname = f"""CO-{name}"""
    out.append(f"""!echo add the HPs""")

    if not combat():
      # finish off
      out.append(f"""There should be an active combat at this point.""")
    else:        
        # locate the group
        group = combat().get_group(groupname, True)
        if not group:
            out.append(f"""-buff should only execute after the original !i madd from running the alias normally.""")
        else:
            numHP = group.combatants[0].max_hp + parsedArgs.last("buff", 0, int)

            messages = []
            messages.append(f"""{ch.name} applies a max hp / temp hp to some critters.""")

            # add the HP to all creatures
            for (critter) in group.combatants:
                critter.set_maxhp(numHP)
                critter.set_hp(numHP)   

                messages.append(f"""{critter.monster_name} ({critter.name}) ({critter.hp}/{critter.max_hp})""")
            
            msg = "\n".join(messages)
            out.append(f"""!embed -desc "{msg}" """)
</drac2>


!echo ... intermission 2 ...
<drac2>
    out = []
    groupname = f"""CO-{name}"""
    buff = parsedArgs.last("buff", 0, int)

    if (buff > 0):
        if not combat():
            # finish off
            out.append(f"""There should be an active combat at this point.""")
        else:        
            # locate the group
            group = combat().get_group(groupname, True)
            numHP = group.combatants[0].max_hp + buff
            if not group:
                out.append(f"""-buff should only execute after the original !i madd from running the alias normally.""")
            else:
                messages = []
                messages.append(f"""{ch.name} applies a max hp / temp hp to some critters.""")

                # add the HP to all creatures
                for (critter) in group.combatants:
                    critter.set_maxhp(numHP)
                    critter.set_hp(numHP)   

                    messages.append(f"""{critter.monster_name} ({critter.name}) ({critter.hp}/{critter.max_hp})""")
                
                msg = "\n".join(messages)
                out.append(f"""!embed -desc "{msg}" """)

    return "\n".join(out)
</drac2>

    
  group = combat().get_group(groupname, True)
  if not group:
    out.append(f"""-finish should only execute after the original !i madd from running the alias normally.""")

  else:
      critter = group.combatants[0]
      creature = f""" "{critter.monster_name}" """

      CR = critter.levels.total_level
      if (CR < 0.25):
          CR = 0.25

      numSummon = int(2 / CR) - 1

      if (numSummon > 0):
          addCmd = f"""!i madd {creature} {commonPart} -n {numSummon} """
          out.append(addCmd)