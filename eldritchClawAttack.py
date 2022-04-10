<drac2>
#too much typing!
ect = "Eldritch Claw Tattoo"
c,ch = combat(),character()
eff = f"Eldritch Maul|As a bonus action, you can empower the tattoo for 1 minute. For the duration, each of your melee attacks with a weapon or an unarmed strike can reach a target up to 15 feet away from you, as inky tendrils launch toward the target. In addition, your melee attacks deal an extra 1d6 force damage on a hit. Once used, this bonus action can't be used again until the next dawn."
base = f"Magical Strikes.|While the tattoo is on your skin, your unarmed strikes are considered magical for the purpose of overcoming immunity and resistance to nonmagical attacks, and you gain a +1 bonus to attack and damage rolls with unarmed strikes."

# are we a Circle of Shepherd druid (!level Druid Shepherd)
monk = load_json(get("subclass", "{}")).get("MonkLevel", "").lower()
force = f'-d "1d6[force]" -f "{eff}"'

if not monk or MonkLevel < 6:
  output = f'-f "{base}" magical -b 1 -d 1 '
else:
  # Monks are already magical
  output = f'-f "{base}" -b 1 -d 1 '
  force = f'-d "1d6[magical force]" -f "{eff}"'


# is the effect there?
if c:
  if c.me.get_effect(ect):
    output = output + " " + force
else:
  output = output + f''' -f "Outside combat, can't verify if ecmaul should apply or not, add a 1d6 if it does."'''

return output
</drac2>