embed <drac2>
companions = load_json(get('companions', "{}"))
out,args,pa = [],&ARGS&,argparse("&*&".lower())

cname = pa.last("name", None)
perception = pa.last("p", None)
creature = pa.last("creature", None)
senses = pa.last("senses")
keen = pa.last("keen")

if not (cname and perception and creature):
  out.append('''-f "You must specify:|* -name - the creature's name (quoted if it contains spaces)
* -p - the creature's perception bonus (or wis bonus if it isn't listed)
* -creature - what it is (warhorse, etc.)" -f "You may also specify:|* -senses - the creature's senses (quoted if there is a space)
* -keen - the creature's keen senses, if any (quoted if there is a space)"''')
else:
  x = {}
  x["perception"]=perception
  x["creature"]=creature

  if senses:
    x["senses"]=senses

  if keen:
    x["keen"]= keen
    
  x["active"]= True

  companions[cname] = x

character().set_cvar('companions', dump_json(companions))

help = """!companion add <-name \\"name\\"> <-p #> <-creature CreatureName> [-sense name] [-keen name]"""

text = " ".join(out)
return f"""-footer "{help}" {out}"""
</drac2> -title "<name> adds <their> companion <cname>" -color <color> -thumb <image>