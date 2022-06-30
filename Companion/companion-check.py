multiline 
<drac2>
companions = load_json(get('companions', "{}"))
out,args,pa = [],&ARGS&,argparse("&*&".lower())

# default to perception
check = "perception"

if len(args) > 0:
  check = args[0]

num = 0

for x in companions:
  entry = companions[x]

  if entry.active:
    #add to initiative
    n = x.replace('"', '\\"')
    a = ctx.author.display_name.replace('"', '\\"')
    num += 1
    out.append(f'''!mc "{entry.creature}" "{check}" -title "{n} ({entry.creature}) makes a {check} check."''')

if 0 == num:
    out.append(f'''!embed -Title "<name> needs to add companions first." -Desc "Use `!companion add` or `!companion activate` before using `!companion check`." -thumb <image> -color <color>''')

return "\n".join(out)
</drac2>
