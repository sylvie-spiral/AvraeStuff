embed <drac2>
companions = load_json(get('companions', "{}"))
out,args,pa = [],&ARGS&,argparse("&*&".lower())

name = pa.last("name")

x = companions.get("name", None) 
if x:
  x.active = False
  out.append('''-desc "{name} is now inactive."''')
  companions["name"] = x
else:
  out.append('''-desc "{name} wasn't found among companion creatures."''')

character().set_cvar('companions', dump_json(companions))

help = """!companion deactivate <-name \\"name\\"> <-p #> <-creature CreatureName> [-sense name] [-keen name]"""

text = " ".join(out)
return f"""-footer "{help}" {out}"""
</drac2> -title "<name> deactivates <their> companion <name>" -color <color> -thumb <image>