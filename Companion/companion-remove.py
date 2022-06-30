embed <drac2>
companions = load_json(get('companions', "{}"))
out,args,pa = [],&ARGS&,argparse("&*&".lower())
help = """!companion remove <\\"name\\">"""
text = ""

if len(args) == 0:
  return f'''-desc "You need to include at least a partial name of the companion to remove." -footer "{help}" {text}'''

cname = args[0]
matches = []

for creature in companions:
  if cname.lower() in creature.lower():
    matches.append(creature)

for creature in matches:
  companions.pop(creature)
  out.append(f'''-f "{creature} was removed."''')

if len(matches) == 0:
  out.append(f'''-desc "{cname} wasn't found among companion creatures."''')

character().set_cvar('companions', dump_json(companions))

text = " ".join(out)
return f"""-footer "{help}" {text}"""
</drac2> -title "<name> removes <their> companion." -color <color> -thumb <image>