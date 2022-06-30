embed <drac2>
companions = load_json(get('companions', "{}"))
out,args,pa = [],&ARGS&,argparse("&*&".lower())
text = ''

help = """!companion deactivate <\\"name\\"> -footer "{help}" {text}"""

if len(args) == 0:
  return f'''-desc "You must specify at least a partial name." '''

cname = args[0]
matches = []

for creature in companions:
  if cname.lower() in creature.lower():
    matches.append(creature)

for creature in matches:
  x = companions[creature]
  x["active"] = False
  out.append(f'''-f "{creature}| {creature} is now inactive."''')
  companions[creature] = x

if len(matches) == 0:
  out.append(f'''-desc "{cname} wasn't found among companion creatures."''')

character().set_cvar('companions', dump_json(companions))

help = """!companion deactivate <\\"name\\">"""

text = " ".join(out)
return f"""-footer "{help}" {text}"""

</drac2> -title "<name> deactivates <their> companion <cname>" -color <color> -thumb <image>
