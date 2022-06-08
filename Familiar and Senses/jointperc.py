c perception
<drac2>
pa = argparse("&*&")
ar = [x.lower() for x in &ARGS&]
args = &ARGS&

out = []
ch = character()

adv = "adv" in ar
dis = "dis" in ar

out.append(" ".join(args))

mySenses = get('senses')

if mySenses:
  if mySenses.find("[")==0:
    # array
    mySenses = load_json(mySenses)
  else:
    # list
    mySenses = mySenses.split(",")

if mySenses:
  text = ", ".join(mySenses)
  out.append(f'-f "{name} Perception|Special Senses ({text})" ')

title = f'-title "{name} makes a perception check."'

if get("familiarData"):
  fd = load_json(get("familiarData"))

  if fd:
    fname = fd.get('name', "[use `!familiar name`]")
    ftype = fd.get('type', "[use `!familiar set type`]")

  allfi = load_json(get_gvar("8623c1d5-c795-4fe3-a812-e008cee66e5a"))

  if ftype:
    fi = allfi.get(ftype.lower())

  title = f'-title "<name> makes a perception check aided by <their> familiar {fname} the {ftype}."'

  fmod = fi.perception

  famSenses = fi.senses

  if famSenses:
    if famSenses.find("[")==0:
      # array
      famSenses = load_json(famSenses)
    else:
      # list
      famSenses =famSenses.split(",")

    famSenses = ", ".join(famSenses)

    # so... 1d20+...
  mods = str(fmod) + "[perception]"

  if adv:
    dice = f"""2d20kh1+{mods}"""
  elif dis:
    dice = f"""2d20kl1+{mods}"""  
  else:
    dice = f"""1d20+{mods}"""

  a = vroll(dice)

  if famSenses:
    out.append(f'-f "{fname} Perception ({famSenses})| {a}"')
  else:
    out.append(f'-f "{fname} Perception | {a}"')

  # if the familiar has at least one keen sense...
  if (len(fi.keen) > 0):
    # this is the first die in the vroll result.
    b = int(a.raw.left.left.values[0].values[0])
    
    if dis:
      # we rolled two dice for its perception, but for the keen sense, only the first counts.
      v = vroll(f"""{b}+{fmod}""")

      out.append(f"""-f "{fname} - {fi.keen} | {v}" """)
    elif not adv:
      # if we rolled at advantage, we're done - otherwise keep the die we rolled above,
      # and roll one additional die for the keen sense - keeping the high
      dice = f"""({b},d20)kh1+{fmod}"""
      b = vroll(dice)
      out.append(f"""-f "{fname} - {fi.keen} (advantage) | {b}" """)
else:
  out.append('''-f "Error|Please use `!familiar set <creature type>` and `!familiar set <familiar name>` before using this alias."''')

out.append(f'''-f "help | !jointPerc [applicable snippets to your own check]"''')
out.append(title)

return " ".join(out)
</drac2>
-color <color> -thumb <image> 