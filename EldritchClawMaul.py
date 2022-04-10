<drac2>
#too much typing!
ect = "Eldritch Claw Tattoo"
c,ch = combat(),character()
eff = f"Eldritch Maul|As a bonus action, you can empower the tattoo for 1 minute. For the duration, each of your melee attacks with a weapon or an unarmed strike can reach a target up to 15 feet away from you, as inky tendrils launch toward the target. In addition, your melee attacks deal an extra 1d6 force damage on a hit. Once used, this bonus action can't be used again until the next dawn."

force = f'-d "1d6[magical force]" -f "{eff}"'
output = ""

# is the effect there?
if c:
  if c.me.get_effect(ect):
    output = output + " " + force
else:
  output = output + " " + force + f''' -f "ecmaul outside of combat can't verify the prior use of `!eldritchClaw`"'''

return output
</drac2>