multiline
<drac2>
o,ms,ch,pa,args = [],[],character(),argparse("&*&"),&ARGS&

i,bd,ls = pa.last("i"),int(pa.last("band", -1)),"list" in args

cr = {1:["CR 0","CR 1/8","CR 1/4"],2:["CR 1/2"],3:["CR 1"],4:["CR 2"],5:["CR 3"],6:["CR 4"],7:["CR 5"],8:["CR 6"],9:["CR 7"],10:["CR 8"],11:["CR 9"]}
if bd > len(cr):
  bd = -1

using(
    nameLib = "e38598a0-1678-496c-b816-664be45c6a98"
)

bhp,grp,aSP = 0,f'{nameLib.getInitials(name)}-Conjure',load_json(get_gvar("9e91a358-654e-45cc-b7bd-94365858e88c"))

spell,ws = None,None

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
    if kl.find(a1) == 0:
      spell = f"""Conjure {k}"""
      ws = v
      its.append(k)

    if a1 == kl:
      ex = True          
      break
  
  if ex or len(its) == 1:
      ms.append(f'**{spell}**')
      l = int(pa.last("l", ws.level))
  else:
    ms.append(f'The following spells match {a1}:')
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
      if ws.filter:
        ms.append(f"Please specify a CR or band for {spell}.")
        for x in range(1, ws.maxBand + 1):
          bd = cr[x]
          c = bd[0]
          ns = ws.ns.get(c,1)
          ms.append(f'* band {x}: {bd} - {ns} respond')

        ms.append("")
        ms.append(f"`!conjure '{a1}' list -band #`")
      else:
        flt = []
        for x in cr:
          for y in cr[x]:
            flt.append(y)
        
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
            its.append(f"{m} ({ii.Source})")

          bs.update({r: its})

      for j in bs:
        its = bs[j]
        its.sort()
        
        if len(its) > 0:
          ms.append(f"**{j}**")

          col = 0
          txt = ""
          for i in its:
            col = col + 1
            if col % 2 != 1:
              txt = txt + "| " + f"{i:35}\n".replace(" "," ")
            else:
              txt = txt + f"{i:35}"

          ms.append(f"`{txt}`")
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
    else:
      ms.append("Need a long rest? No slot available or not prepared.")
    
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
        ms.append(f"""Couldn't find {c} - {len(its)} matches.""")
      else:
        if not i:
          ch.spellbook.use_slot(l)
          ms.append(ch.spellbook.slots_str(l))

        ns = ws.ns.get(cr,1)
        mul = 1 + int((l - ws.level) / ws.interval)

        co = combat()
        if co:
          g = combat().get_group(grp)
          if g != None:
            o.append(f"""!i remove "{grp}" """)
            ms.append(f"""Removed existing creatures in {grp}""")

          for x in range(0, mul):
            o.append(f"""!i madd "{mm}" -n {ns} -group "{grp}" -controller {ctx.author} -h """)
          
          c1 = co.get_combatant(name, True)
          if c1:
            c1.add_effect(f'{spell} Caster', duration=600, concentration=True)
            o.append(f"""!i effect "{grp}" "{spell}" -parent "{name}|{spell} Caster" """)
            
        else:
          t = mul * ns
          ms.append(f"""{t} {mm} respond.""")
    
    if ws:
      ms.append(f"""{ws.desc}""")

  else:
    ms.append(f"""Couldn't find "{a1}" """)

dt = "\n".join(ms)
o.append(f"""!embed -desc "{dt}" -footer {get_gvar("cc2f3710-f08e-4e7a-8f18-476252a1614f")} """)

return "\n".join(o)
</drac2>
