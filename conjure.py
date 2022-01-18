multiline
<drac2>
  out = []
  ch = character()

  parsedArgs = argparse("&*&")
  args = &ARGS&

  i = parsedArgs.last("i")

  bhp = 0
  
  grp = f"""CO-{name}"""

  allSpells = load_json(get_gvar("9e91a358-654e-45cc-b7bd-94365858e88c"))

  druidL = ch.levels.get("Druid")
  isShep = False
  if (druidL >= 3):
    if ("subclass" in ch.cvars):
      subc = load_json(ch.cvars["subclass"]).get("DruidLevel","")

    if subc == "Shepherd":
      isShep = True

  msg = []

  if (len(args) < 2) or args[0] == "help" or args[0] == "?":
    for t in allSpells:
      msg.append(f"""* {t}""")
  elif (args[0] == "list"):    
    for t in allSpells:
      if not args[1].lower() in t.lower():
        continue

      g = allSpells.get(t)

      data = get_gvar(g.gvar)
      ratings = load_json(data)
    
      msg.append(f"""**Conjure {t}**""")

      for r in ratings:
        msg.append(f"""*{r}*""")
        items = []
        curr = ratings.get(r)
        for m in curr:          
          info = curr.get(m)
          items.append(f"""{m} ({info.Source})""")

        msg.append(", ".join(items))
        msg.append("")
      
      break
  else:
    spell = None
    which = None
    for t in allSpells:
      if not args[0].lower() in t.lower():
        continue

      spell = f"""Conjure {t}"""

      which = allSpells.get(t)
      msg.append(f"""*{ch.name} casts {spell}*.""")
      break

    if which == None:
      msg.append(f"""Couldn't find {args[0]}.""")
    else:
      who = False
      rating = ""
      cre = ""

      data = get_gvar(which.gvar)

      ratings = load_json(data)

      cre = args[1].lower()
      exact = False
      count = 0
      w = None
      tc = cre

      for r in ratings:
        curr = ratings.get(r)

        for k,v in curr.items():
          if exact:
            break

          l = k.lower()

          if cre == l:
            exact = True
            who = v
            rating = r            
            cre = k            
          elif cre in l:
            w = v
            rating = r
            tc = k            
            count = count + 1            

        if not exact:
          who = w        
          cre = tc

      if not who or (not exact and count > 1):
        msg.append(f"""{count} matches for {cre}""")        
      else:
        sl = parsedArgs.last("l", which.level, int)
        if not sl:
          sl = which.level
  
        cast = False
        if i:
          msg.append("Ignored resources.")
          cast = True
        elif sl >= which.level and ch.spellbook.can_cast(spell, sl):
          ch.spellbook.cast(spell, sl)
          msg.append(ch.spellbook.slots_str(sl))
          cast = True
          
        if not cast:
          msg.append("Could not cast the spell.")
        else:
          msg.append(f"""{ch.name} is conjuring {cre} ({rating})""")

          ns = which.ns.get(rating)
          
          mult = 1 + int((sl - which.level) / which.interval)

          ns = ns * mult

          msg.append(f"""{ns} respond to the call.""")

          if (isShep) and (which.shep):
            bhp = bhp + who.HD * 2
            msg.append(f"""Mighty Summoner +{bhp} hp.""")

          if (combat()):
            hp = who.HP + bhp             
            out.append(f"""!i madd "{cre}" -group "{grp}" -n {ns} -hp {hp} -controller "{ctx.author.name}#{ctx.author.discriminator}" -h""")

  desc = "\n".join(msg)

  cmd = f"""!embed -desc "{desc}" -footer "!conjure list <spell> | !conjure <spell> <creature> [-l #] [-i] - @SylvieTG#4737" """
  out.append(cmd)

  return "\n".join(out)
</drac2>
