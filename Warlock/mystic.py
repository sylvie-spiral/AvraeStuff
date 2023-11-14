multiline <drac2>
o,ch,args,errMsg = [],character(),&ARGS&,None

footer = 'Usage: !mystic <name-of-spell> [... targets, snippets, etc. ...]'

# does the requested ability exist
requested = args[0] if len(args) > 0 else None

if (requested):
  cc = ch.cc(requested) if ch.cc_exists(requested) else None;  
  if (cc == None):
    results = []
    for x in ch.consumables:
      if requested.lower() in x.name.lower():
        results.append(x.name)

    if len(results) == 1:
      cc = ch.cc(results[0])
    elif len(results) > 1:
      strResults = '\n'.join(results)
      errMsg = f"{len(results)} matches for {requested}. {strResults}."

  if (cc):
    title = cc.name
    spell = title.split(':')[1].strip()

    if (cc.value > 0):
      cc.mod(-1)
      o.append(f"""!echo {spell}""")
      cmd = f"""!cast "{spell}" -i {' '.join(args)} -f "{title}:{ch.cc_str(title)} (**-1**)" """

      o.append(f"""!echo {cmd}""")
    else:  
      errMsg = f"{ch.name} has no remaining uses of {title}"
  else:
    if len(errMsg) == 0:
      errMsg = f"No matches for {requested}. Please check the name and try again."
else:
  errMsg = f"{ch.name} needs to specify a spell they are casting."

if (errMsg):
  o.append(f"""!embed -desc "{errMsg}" -title "Mystic Arcanum" """)

out = "\n".join(o)
return f"""{out} -footer "{footer}" """

</drac2>