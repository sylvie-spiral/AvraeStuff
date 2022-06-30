multiline 
<drac2>
companions = load_json(get('companions', "{}"))
out = []
num = 0

for x in companions:
  entry = companions[x]

  if entry.active:
    #add to initiative
    n = x.replace('"', '\\"')
    a = ctx.author.display_name.replace('"', '\\"')
    num += 1
    out.append(f'''!i madd "{entry.creature}" -name "{n}" -conctroller "{a}"''')

if 0 == num:
    out.append(f'''!embed -Title "<name> needs to add companions first." -Desc "Use `!companion add` or `!companion activate` before using `!companion join`." -thumb <image> -color <color>''')

return "\n".join(out)
</drac2>