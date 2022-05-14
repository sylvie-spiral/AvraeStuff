multiline 
<drac2>
companions = load_json(get('companions', "{}"))
out = []
num = 0

for x in companions:
  entry = companions[x]

  if entry.active:
    #add to initiative
    n = entry.name.replace('"', '\\"')
    num += 1
    out.append(f'''!i madd "{entry.creature}" -name "{n}" ''')

if 0 == num:
    out.append(f'''!embed -Title "<name> needs to add companions first." -Desc "Use `!companion add` or `!companion active` before using `!companion init`." -thumb <image> -color <color>''')

return "\n".join(out)
</drac2>