!alias jointperc multiline
<drac2>
args= "&ARGS&"
out = []

fd = load_json(get("familiarData"))
fname = fd.name
ftype = fd.type

allfi = load_json(get_gvar("8623c1d5-c795-4fe3-a812-e008cee66e5a"))
fi = allfi.get(ftype.lower())

fmod = fi.perception

#follow character's pronouns if !pronouns has been used
they = get("they","they")
their = get("their","their")
them = get("them","them")
theirs = get("theirs","theirs")

adv = "adv" in args
dis = "dis" in args

if adv and dis:
  adv = 0
  dis = 0

# get mod from character sheet
mod = get_raw().skills.perception

# handle disadvantage, advantage, etc.
if dis:
  dice = "2d20kl1+"
elif adv:
  dice = "2d20kh1+"
else:
  dice = "1d20+"

dice = dice + str(mod) +"[perception]"

if "guide" in args:
  dice = dice + "+1d4[guidance]"

check = vroll(dice)

# so... 1d20+...
mods = str(fmod) + "[perception]"

if adv:
  dice = f"""2d20kh1+{mods}"""
elif dis:
  dice = f"""2d20kl1+{mods}"""  
else:
  dice = f"""1d20+{mods}"""

cmd = f"""!embed -title "{name} makes a Perception check!" -desc "{name} looks around the area, while {their} familiar, {fname} - the {ftype}, keep watch. {fi.senses}" -f "{name} Perception | {check}" """

a = vroll(dice)

cmd = cmd + f"""-f "{fname} Pereception | {a}" """

# if the familiar has at least one keen sense...
if (len(fi.keen) > 0):
  if dis:
    # we rolled two dice for its perception, but for the keen sense, only the first counts.
    b = int(a.raw.left.left.values[0].values[0])
    v = vroll(f"""{b}+{fmod}""")

    cmd = cmd + f"""-f "{fname} - {fi.keen} | {v}" """
  elif not adv:
    # if we rolled at advantage, we're done - otherwise keep the die we rolled above,
    # and roll one additional die for the keen sense - keeping the high
    b = int(a.raw.left.left.values[0].values[0])

    dice = f"""({b},d20)kh1+{fmod}"""
    b = vroll(dice)
    cmd = cmd + f"""-f "{fname} - {fi.keen} (advantage) | {b}" """

out.append(cmd)

return "\n".join(out)
</drac2>
