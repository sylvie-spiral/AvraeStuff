multiline
<drac2>
o,a,pa,msg = [],&ARGS&,argparse("&*&".lower()),[]
dragonwingbow = get("dragonwingbow",{})

ch = character()
dt = pa.last('dt')
ok = 0
item = pa.last('name')
allowed = ["acid", "cold", "fire", "force", "lightning", "necrotic", "poison", "psychic", "radiant", "thunder"]

if not item:
  item = "dragon wing"

if dt:
  ok = dt in allowed    
else:
  msg.append(f'You need to specify `-dt` with one of {allowed}.')

if ok:
  for a in ch.attacks:
    if item in a.name.lower():
      ok = 1
      ef = a.raw.automation[0].effects[0]
      txt = a.raw.automation[1].text
    
      dmg = ef.hit[0].damage
      parts = dmg.split(" + ")      
      ch.set_cvar("dragonwingbow", dragonwingbow)
      base = " + ".join([parts[0],f"1d6[magical {dt}]"])

      #create new attack
      o.append(f"""!a add "dwb" -d "{base}" -b "{ef.attackBonus}" -desc "{txt}" """)

  if not ok:
    msg.append(f"Couldn't locate {item} did you rename it in D&D Beyond? If so, use -name to tell me what to look for!")

if ok:
  msg.append(f"""Congratulations, your fancy new bow is ready to go!

  Use `!dwb` or `!a dwb` to attack and your {dt} damage will be added automatically!
  
  If you subscribe to the `!pronouns` workshop and have selected them for your character,
  they will be respected by this alias.""")
  m = "\n".join(msg)

  o.append(f"""!embed -desc "{m}" -title '{name} needs help setting up a Dragon Wing Bow'""")
else:
  msg.append("")
  msg.append("To set up this item and update your attack:")
  msg.append("`!dragonWingBow <-dt damage type> [-name 'Dragon Wing Longbow']")
  msg.append("")
  msg.append(f"Replace fire with one of {allowed}")
  msg.append("You only need to specify the name if you have renamed the item to not start with 'Dragon Wing'")
  msg.append("")
  msg.append("To execute afterwards, use the attack as normal.")

  m = "\n".join(msg)
  o.append(f"""!embed -desc "{m}" -title '{name} needs help setting up a Dragon Wing Bow'""")

return "\n".join(o)
</drac2>