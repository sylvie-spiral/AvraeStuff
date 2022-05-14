multiline
<drac2>
o,ms,ch,pa,args,c = [],[],character(),argparse("&*&"),&ARGS&,combat()
t = pa.last("t", name)
l = max(int(pa.last("l", 4)),4)
i = pa.last("i")
grp = f'POLY-{t}'
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
        real = j

  else:
    if not real:      
      real = c.me
      isSelf = True

  isSelf = (real.name == name)

if isSelf:
  ms.append(f"*{name} casts Polymorph!*")
elif real:
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
  ms.append(f'You need to specify -c <creature> such as `!polymorph -c Wolf`')
elif i or ch.spellbook.can_cast("Polymorph", l):
  ex,its, ii = 0, [], None

  ms.append(f"""This spell transforms a creature that you can see within range into a new form. An unwilling creature must make a Wisdom saving throw to avoid the effect. The spell has no effect on a shapechanger or a creature with 0 hit points.

The transformation lasts for the duration, or until the target drops to 0 hit points or dies. The new form can be any beast whose challenge rating is equal to or less than the target's (or the target's level, if it doesn't have a challenge rating). The target's game statistics, including mental ability scores, are replaced by the statistics of the chosen beast. It retains its alignment and personality.

The target assumes the hit points of its new form. When it reverts to its normal form, the creature returns to the number of hit points it had before it transformed. If it reverts as a result of dropping to 0 hit points, any excess damage carries over to its normal form. As long as the excess damage doesn't reduce the creature's normal form to 0 hit points, it isn't knocked unconscious.

The creature is limited in the actions it can perform by the nature of its new form, and it can't speak, cast spells, or take any other action that requires hands or speech.

The target's gear melds into the new form. The creature can't activate, use, wield, or otherwise benefit from any of its equipment.)""")

  if c:
    if ok:
      for lv in range(2, tl + 1):
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
              cr = r

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
      else:
        ms.append(f'Found creature {its[0]}')
        if not i:
          ch.spellbook.cast("Polymorph", l)

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
          ft = "**Specified -fail to autofail**"
        elif fail:
          ft = "**Failed!**"
        else:
          ft = "**succeeded!**"
        ms.append(f'*{real}*: {r} - DC {dc} - {ft}')

        if fail:          
          grp = f'POLY-{real.name}'
          real.set_group(grp)

          extra = ""
          if isSelf:
            extra = """-note "Needs a !ms con after damage (concentration)" """

          o.append(f'!i madd {creature} -group {grp} -controller {ctx.author} -h {extra}')
          if not isSelf:
            o.append(f'!i effect "{grp}" Polymorph -parent "{name}|Polymorph Caster"')
          else:
            o.append(f'!i effect "{grp}" Polymorph -conc -parent "{name}|Polymorph Caster"')

          if c.me:
            c.me.add_effect("Polymorph Caster", "", duration = 600, concentration=True, desc="If concentration is ended, caster needs to run `!polymorph end`")

          o.append(f'!monimage {creature}')
  else:
    ms.append(f'Not currently in combat. (repeat with -i when combat happens)')    
elif not i:
  ms.append(f"Can't cast at {l} - {ch.spellbook.slots_str(l)}")


dt = "\n".join(ms)
extra = ""
if len(fields):
  "-f ".join(fields)

o.append(f"""!embed -desc "{dt}" -footer "!polymorph <-c creature> [-l #] [-i] [-t target] | !polymorph end [-d #] [-t target]" {extra}""")
o.reverse()
return "\n".join(o)
</drac2>