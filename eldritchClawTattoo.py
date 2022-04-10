embed
<drac2>
pa,args,ch,c = argparse("&*&"),&ARGS&,character(),combat()
ignore = pa.last("i")
reset_counter = pa.last("reset")
they,their,them,theirs = get("they","they"),get("their","their"),get("them","them"),get("theirs","theirs")

#too much typing!
ect = "Eldritch Claw Tattoo"
eft = "As a bonus action, you can empower the tattoo for 1 minute. For the duration, each of your melee attacks with a weapon or an unarmed strike can reach a target up to 15 feet away from you, as inky tendrils launch toward the target. In addition, your melee attacks deal an extra 1d6 force damage on a hit. Once used, this bonus action can't be used again until the next dawn."

#create the counter if needed
ch.create_cc_nx(ect, 0, 1, "long", "bubble", 1, None, ect, eft)

out = []
fields = []
hasResource = ignore

if ignore:
  out.append("**(ignore resources)**")
  hasResource = True
elif reset_counter:
  ch.set_cc(ect, ch.cc(ect).max)
  out.append("**(reset counter)**")
  fields.append(f'''"{ect}|Counter reset."''')  
else:
  if ch.get_cc(ect) > 0:
    hasResource = True
    ch.mod_cc(ect, -1)

fields.append(f'''"{ect}|{ch.cc_str(ect)}"''')

if hasResource:
  out.append(f"{ch.name} activates {their} Eldritch Claw Tattoo as a bonus action.")
  if c and c.me:
    # Add a marker effect
    c.me.add_effect(ect, "", duration=10, desc=eft)
  else:
    if c:
      out.append("You are not in the current combat, please `!i join` and repeat with -i")
    else:
      # out of combat
      out.append("Please remember to use the alias again with `-i` if appropriate after initiative starts.")
else:
  if not reset_counter:
    out.append(f"""{ch.name} attempts to use {their} Eldritch Claw Tattoo, but is out of uses.
    * If you started out of combat, you may need -i
    * You might need a long rest
    * If this is genuinely incorrect, use -reset and tell a Technomancer.""")

out.append(eft)

ft = " -f ".join(fields)
text = "\n".join(out)

return f'''-desc "{text}" -title "{ect}" {ft}'''
</drac2>