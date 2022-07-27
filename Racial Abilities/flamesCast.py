!alias flamesCast cast &*& <drac2>
args, out = argparse(&ARGS&), [] 

feats = load_json(character().cvars.feats.lower())

# check the feat
if not "flames of phlegethos" in feats:
    return "-f 'Flames of Phlegethos|You do not have the Flames of Phlegethos feat. If this is incorrect, please add it before using this command.'"

c = combat()

if c:
    c.me.add_effect("Flames of Phlegethos", desc="The flames shed bright light out to 30 feet and dim light for an additional 30 feet. While the flames are present, any creature within 5 feet of you that hits you with a melee attack takes 1d4 fire damage.",duration=2,end=True)    
    out.append(f'''-f "Flames of Phlegethos|When you roll fire damage for a spell you cast, you can reroll any roll of 1 on the fire damage dice, but you must use the new roll, even if it is another 1. (use `!flamesReroll -d 1d10`)" ''')
    out.append(f'''-f "Flames of Phlegethos|Whenever you cast a spell that deals fire damage, you can cause flames to wreathe you until the end of your next turn. The flames don't harm you or your possessions"  ''')    

return " ".join(out)

</drac2> -color <color> -thumb <image> -footer """!flamesCast spell [see `!cast` or the workshops for applicable snippets] | Avrae Technomancers"""