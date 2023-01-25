multiline
<drac2>
o,ms,ch,pa,args,c = [],[],character(),argparse("&*&"),&ARGS&,combat()

t = pa.last("t", name)

grp = f'POLY-{t}'
fields = []

isSelf = True
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


else:
  isSelf = (t == name)

ms.append(f"*{name} ends a polymoprh spell.*")
ms.append("""The target assumes the hit points of its new form. When it reverts to its normal form, the creature returns to the number of hit points it had before it transformed. If it reverts as a result of dropping to 0 hit points, any excess damage carries over to its normal form. As long as the excess damage doesn't reduce the creature's normal form to 0 hit points, it isn't knocked unconscious.""")

if real:
  ms.append(f"{real.name} is targetted by a polymorph spell.")

if poly:
  ms.append(f"{poly.name} is the beast they were changed into.")

if c:
  if poly:
    o.append(f'!i remove {poly.name}')
    o.append(f'!i opt "{real.name}" -group None')

  if real:
    real.set_group(None)
    d = int(pa.last("d", 0))
    # find the beast in the group:
    if poly:
      carry = 0 - min(poly.hp, 0)
      ms.append(f'Carry over damage from {poly.name} is {carry}.')
      if carry > 0:
        real.damage(f'{carry}')
        
      ms.append(f"{real.name} <{real.hp}/{real.max_hp}> ({carry}) ")          
    else:
      ms.append(f"Couldn't locate the polymorphed creature")

    real.remove_effect("Polymorph")
  else:
    if isSelf:
      ch.modify_hp(0 - d)
      ms.append(f"{name} <{hp}/{max_hp}> (-{d})")
elif not real:
  ms.append(f"Couldn't locate the real person.")

dt = "\n".join(ms)

o.append(f"""!embed -desc "{dt}" -footer "!polymorph end [-d #] [-t target]" """)
return "\n".join(o)
</drac2>