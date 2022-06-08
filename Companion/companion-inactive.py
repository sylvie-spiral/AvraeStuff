embed <drac2>
companions = load_json(get('companions', "{}"))
out,args,pa = [],&ARGS&,argparse("&*&".lower())

cname = pa.last("name")
matches = []

for creature in companions:
  if cname in creature:
    matches.append(creature)

for creature in matches:
  x = companions[creature]
  x["active"] = False
  out.append(f'''-f "{creature}| {creature} is now inactive."''')
  companions["name"] = x

if len(matches) == 0:
  out.append(f'''-desc "{cname} wasn't found among companion creatures."''')

character().set_cvar('companions', dump_json(companions))

help = """!companion deactivate <-name \\"name\\"> <-p #> <-creature CreatureName> [-sense name] [-keen name]"""

text = " ".join(out)
return f"""-footer "{help}" {text}"""

</drac2> -title "<name> deactivates <their> companion <cname>" -color <color> -thumb <image>
