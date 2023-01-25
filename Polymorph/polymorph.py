multiline
<drac2>
using(
    nameLib = "e38598a0-1678-496c-b816-664be45c6a98"
)

o,ms,ch,pa,args,c = [],[],character(),argparse("&*&"),&ARGS&,combat()
ex,its, ii, act_cr = 0, [], None, ""
t = pa.last("t", name)
l = max(int(pa.last("l", 4)),4)
i = pa.last("i")
grp = f'{nameLib.getInitials(t)}-Polymorph'
fields = []
fail = pa.last("f")
isSelf = True
ok = False
adv = None
if "adv" in args:
  adv = True
elif "dis" in args:
  adv = False

tl = 20

creature = pa.last("c", "").lower()
ls = pa.last("list", None)

cr = ["CR 0","CR 1/8","CR 1/4","CR 1/2","CR 1"]

#these are from conjure's data
lists = ["5517ee08-0888-479e-be8c-76b7e2f14c40","c84d0405-6961-4f29-a43c-7583d4546cbf"]

poly,real = None,None

if c:
  if t:
    real = c.get_combatant(t)
    if real:
      grp = real.group

  g = c.get_group(grp)
  if g:
    for j in g.combatants:
      if j.creature_type == "beast":
        poly = j

  else:
    if not real:      
      real = c.me
      isSelf = True

  isSelf = (real) and (real.name == name)
else:
  if t == name:
    real = ch
    isSelf = True
  else:
    ms.append(f"Outside of combat can't enforce CR except on self.")

#if isSelf:
#  ms.append(f"*{name} casts Polymorph!*")
if real:
  if isSelf:
    ms.append(f"*{name} casts Polymorph on themself!*")
  else:
    ms.append(f"*{name} casts Polymorph on {real.name}!*")
  tl = real.levels.total_level
  ok = True
else:
  ms.append(f"*{name} casts Polymorph on {t}")

ms.append("")

if c and not real:
  ms.append(f"""Couldn't find a target {t} - is there a typo? ({grp})""")

if isSelf:
  fail = True

if len(creature) == 0:
  ms.append(f'You need to specify `-c <creature>` such as `!polymorph -c Wolf`')
  ms.append(f'You can use `-f` to make the saving throw automatically fail on a willing target.')
  ms.append(f'You do not need to use `-f` if you are targetting yourself.')
  ms.append(f'Use `-t target` to target someone or something else, `-l` to use a higher level slot or `-i` to ignore requirements')
  ok = False
else:
  for lv in range(2, int(tl) + 1):
    cr.append(f'CR {lv}')

  for j in lists:
    if ex:
      break

    rat = load_json(get_gvar(j))

    for r in rat:
      if not r in cr:
        continue
      
      if ex:
        break

      am = rat.get(r)

      for m in am:
        ml = m.lower()
        if creature in ml:
          ii = m
          its.append(m)
          mm = ml
          act_cr = r

          if ml == creature:
            its = [m]
            ex = 1
            break

  if (len(its)>1) or (len(its) == 0):
    ms.append(f"""Couldn't find {creature} - {len(its)} matches.""")
    if (len(its) <= 5):
      for j in its:
        ms.append(f"* {j}")
    
    el = ", ".join(cr)
    ms.append(f"Eligible CRs: {el}")
    ok = False
  else:        
    creature = its[0]
    ms.append(f'Found creature {creature} [{act_cr}]')

canCast = (i or ch.spellbook.can_cast("Polymorph", l))

if ok and canCast:
  if not i:
    ch.spellbook.cast("Polymorph", l)

  if c and len(its) == 1:
    r = real.save("wis",adv)
    dc = ch.spellbook.dc
    if fail:
      r = 0
    elif not isSelf:
      if r.total >= ch.spellbook.dc:
        fail = False
      else:
        fail = True
    
    if isSelf:
      fail = True
      ft = "**Cast on Self**"
    elif r == 0:
      fail = True
      ft = "**Specified `-f` to autofail**"
    elif fail:
      ft = "**Failed!**"
    else:
      ft = "**succeeded!**"
    ms.append(f'*{real}*: {r} - DC {dc} - {ft}')

    if fail:
      # if we're targetting ourselves, use the normal group name.
      # Otherwise, name it for the target instead.      
      if isSelf:
        grp = nameLib.createGroupName(suffix = "Polymorph")
      else:        
        grp = nameLib.createGroupNameTarget(real, suffix = "Polymorph")

      real.set_group(grp)

      extra = ""
      if isSelf:
        extra = """-note "Remember to use creature for concentration checks!" """

      o.append(f'!i madd "{creature}" -group {grp} -controller {ctx.author} -h {extra}')

      if isSelf:
        o.append(f'!i effect "{grp}" Polymorph -conc')
      else:
        c.me.add_effect("Polymorph Caster", duration = 600, concentration=True)
        o.append(f'!i effect "{grp}" Polymorph -parent "{name}|Polymorph Caster"')
elif not i:
  ms.append(f"Can't cast at {l} - {ch.spellbook.slots_str(l)}")

if not c:
  ms.append(f'Not currently in combat. (repeat with -i when combat happens)')    

if ok:
  ms.append("")
  
  if isSelf:
    ms.append(f"""When finished use `!polymorph end` if in combat to end the effect and apply any carry over damage (if the polymorph form is still in initiative).""")
    ms.append(f"""Use `!polymorph end -d #` to specify damage if the creature is already removed""")
  else:
    ms.append(f"""When finished use `!polymorph end -t "{real.name}"` if in combat to end the effect and apply any carry over damage (if the polymorph form is still in initiative).""")
    ms.append(f"""Use `!polymorph end -d # -t "{real.name}"` to specify damage if the creature is already removed""")

dt = "\n".join(ms)
extra = ""
if len(fields):
  "-f ".join(fields)

o.insert(0, f"""!embed -desc "{dt}" -footer "!polymorph <-c creature> [-l #] [-i] [-t target] [-f]" {extra}""")
return "\n".join(o)
</drac2>