embed -desc
<drac2>
c = combat()

groups = {"Characters": [], "Critters":[], "Conjured":[],"Summoned":[],"Groups":[]}
grp = None

if c:  
  for x in c.combatants:
    m = x.levels.get("Monster",-1)

    if m >= 0:
      if (c.me) and (c.me.group) and x.group == c.me.group:
        grp = "Summoned"
      else: 
        match = 0

        # is there a conjure effect?
        for y in x.effects:
          ln = y.name.lower()
          if ln.find('conjure') == 0:
            match = 1
            break

        if match:
          grp = "Conjured"
        else:
          grp = "Critters"
                
    else:
      grp = "Characters"

    if grp:
      groups.get(grp).append(f'-t \\"{x.name}|\\"')

  for y in c.groups:
    groups.Groups.append(f'-t \\"{y.name}|\\"')


  output = f'''"**Best Guesses:** ```'''

  for k in groups:
    g = groups.get(k)
    if len(g):
      t = " ".join(g)
      output = output + f"\n{k:10}: {t}\n"

  output = output + """```" """

  return output
else:
  return '"Start initiative first."'
</drac2> -title "Groups of Targets (for copy/paste)" -thumb <image> -color <color>