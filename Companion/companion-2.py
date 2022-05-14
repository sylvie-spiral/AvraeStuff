embed <drac2>
companions = load_json(get('companions', "{}"))
out,args,pa = [],&ARGS&,argparse("&*&".lower())

name = pa.last("name")
perception = pa.last("p")
creature = pa.last("creature")
x = {}
x.perception = perception
x.creature = creature

x.senses = args.get("senses")
x.keen = args.get("keen")
x.active = True

if not (name and perception and creature):
  out.append('''-f "You must specify:|* -name - the creature's name (quoted if it contains spaces)
* -p - the creature's perception bonus (or wis bonus if it isn't listed)
* -creature - what it is (warhorse, etc.)" -f "You may also specify:|* -senses - the creature's senses (quoted if there is a space)
* -keen - the creature's keen senses, if any (quoted if there is a space)''')
if companions[name]:
  # updating a companion
  companions[name] = x
else:
  # adding a new companion
  companions.add(name, x)

character().set_cvar('companions', dump_json(companions))

help = """!companion add <-name \\"name\\"> <-p #> <-creature CreatureName> [-sense name] [-keen name]"""

text = " ".join(out)
return f"""-footer "{help}" {out}"""
</drac2> -title "<name> adds <their> companion <name>" -color <color> -thumb <image>