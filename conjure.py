multiline
<drac2>
  o = []
  ms = []

  ch = character()

  pa = argparse("&*&")
  args = &ARGS&

  i = pa.last("i")
  bd = int(pa.last("band", -1))
  ls = "list" in args
  shep = load_json(get("subclass", "{}")).get("DruidLevel", "").lower() == "shepherd"

  cr = {1:["CR 0","CR 1/8","CR 1/4"],2:["CR 1/2"],3:["CR 1"],4:["CR 2"]}
  if bd > len(cr):
    bd = -1

  bhp = 0
  
  grp = f"""CO-{name}"""

  aSP = load_json(get_gvar("9e91a358-654e-45cc-b7bd-94365858e88c"))

  spell = None
  ws = None

  if len(args) > 1:
    a1 = args[0].lower()

  if (len(args) < 2):
    ms.append("Supports the following spells:")
    for t in aSP:
      ms.append(f"""* {t}""")
  else:
    its = []
    ex = False
    
    for k in aSP.keys():
      v = aSP.get(k)
      kl = k.lower()
      if a1 in kl:
        spell = f"""Conjure {k}"""
        ws = v
        its.append(k)

        if a1 == kl:
          ex = True          
          break
    
    if ex or len(its) == 1:
       ms.append(f"""**{spell}**""")
       l = int(pa.last("l", ws.level))
    else:
      ms.append(f"""The following spells match {a1}:""")
      ms.append("\n".join(its))
      spell = ""

    if spell and ls:      
      bs = {}
      flt = "NO"

      if bd > 0:
        flt = cr[bd]
      elif (len(args) > 2):
        flt = ["CR " + args[2]]
      else:
        ms.append("Please specify a CR or band.")
        for x in range(1,5):
          ms.append(f"""* bd {x}: {cr[x]} - {ws.ns[cr[x][0]]} respond""")
          
      if flt != "NO":
        g = ws

        for r in flt:
          bs[r] = []

        for j in ws.gvar:
          ratings = load_json(get_gvar(j))

          for r in ratings:
            if not r in flt:
              continue

            its = bs.get(r)
          
            ci = ratings.get(r)
            for m in ci:
              ii = ci.get(m)
              its.append(f"""{m} ({ii.Source})""")

            bs.update({r: its})

        for j in bs:
          its = bs[j]
          its.sort()
          
          ms.append(f"""**{j}**""")
          ms.append(", ".join(its))
          ms.append("")

        ms.append("Use !conjure with the creature the DM chooses.")
    elif spell:
      c = args[1].lower()

      g = 0
      if i:
        ms.append("Ignored resources")
        g = 1
      elif ch.spellbook.can_cast(spell, l):
        g = 1
        ch.spellbook.use_slot(l)
        ms.append(ch.spellbook.slots_str(l))
      else:
        ms.append("Need a long rest? No slot available.")
      
      its = []
      ii = None
      cr = None
      mm = None
      ex = 0

      if g:
        for j in ws.gvar:
          if ex:
            break

          rat = load_json(get_gvar(j))

          for r in rat:
            if ex:
              break

            am = rat.get(r)

            for m in am:
              ml = m.lower()            
              if c in ml:
                ii = am.get(m)
                its.append(ii)
                mm = ml
                cr = r

                if ml == c:
                  its = [ii]
                  ex = 1
                  break
            
        if (ii == None) or (not ex and (len(its)>1)):
          ms.append(f"""Couldn't find {c} - {its}""")
        else:
          hp = ii.HP
          ns = ws.ns[cr]
          shep = shep and ws.shep
          mul = 1 + int((l - ws.level) / ws.interval)

          if shep:
            hp = hp + ii.HD * 2
            ms.append("Mighty Summoner")

          if combat():
            for x in range(0, mul):
              o.append(f"""!i madd "{mm}" -n {ns} -group "CO-{name}" -controller {ctx.author} -h -hp {hp}""")
          else:
            t = mul * ns
            ms.append(f"""{t} {mm} respond.""")

    else:
      ms.append(f"""Couldn't find "{a1}" """)

  dt = "\n".join(ms)
  o.append(f"""!embed -desc "{dt}" -footer {get_gvar("cc2f3710-f08e-4e7a-8f18-476252a1614f")} """)

  return "\n".join(o)
</drac2>
