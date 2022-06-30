embed <drac2>
companions = load_json(get('companions', "{}"))
out,args,pa = [],&ARGS&,argparse("&*&".lower())
help = """!companion activate <\\"name\\">"""
text = ""

if (len(args)) == 0:
  return f"""-desc "You need to specify at least a partial name for the companion to activate." -footer "{help}" {text}"""

cname = args[0]
matches = []

for creature in companions:
  if cname.lower() in creature.lower():
    matches.append(creature)

for creature in matches:
  x = companions[creature]
  x["active"] = True
  out.append(f'''-f "{creature}| {creature} is now active."''')
  companions["name"] = x

if len(matches) == 0:
  out.append(f'''-desc "{cname} wasn't found among companion creatures."''')

character().set_cvar('companions', dump_json(companions))

help = """!companion activate <-name \\"name\\"> <-p #> <-creature CreatureName> [-sense name] [-keen name]"""

text = " ".join(out)
return f"""-footer "{help}" {text}"""
</drac2> -title "<name> activates <their> companion <cname>" -color <color> -thumb <image>