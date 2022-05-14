embed <drac2>
companions = load_json(get('companions', "{}"))
out,args,pa = [],&ARGS&,argparse("&*&".lower())

name = pa.last("name")

if companions.get("name", None):
  companions.remove(name)
  out.append('''-desc "{name} was removed."''')
else:
  out.append('''-desc "{name} wasn't found among companion creatures."''')

character().set_cvar('companions', dump_json(companions))

help = """!companion remove <-name \\"name\\"> <-p #> <-creature CreatureName> [-sense name] [-keen name]"""

text = " ".join(out)
return f"""-footer "{help}" {out}"""
</drac2> -title "<name> removes <their> companion <name>" -color <color> -thumb <image>