embed <drac2>
companions = load_json(get('companions', "[]"))

out = []

for x in companions:
  entry = companions[x]

  status = "inactive"
  if entry.active:
    status = "active"

  out.append(f'''-f "{x}|{entry.type} - {status}"''')

if len(companions) == 0:
  out.append('-f"No Companions Found|Use `!companion add` to add them first."')

return '-desc "Your companions are:" ' + " ".join(out)
</drac2>  -title "<name> checks their companions" -color <color> -thumb <image>