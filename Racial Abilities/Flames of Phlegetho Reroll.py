!alias flamesReroll embed -color <color> -thumb <image> -title "<name> uses <their> Flames of Phlegethos to reroll 1s on fire damage." -footer """!flamesReroll <dice to reroll>  | Avrae Technomancers"""
<drac2>
args, out = argparse(&ARGS&), ['''  -desc "When you roll fire damage for a spell you cast, you can reroll any roll of 1 on the fire damage dice and use the new roll."  '''] 
feats = load_json(character().cvars.feats.lower())

# check the feat
if not "flames of phlegethos" in feats:
    return "-f 'You do not have the Flames of Phlegethos feat. If this is incorrect, please add it before using this command.'"

# tell # and type of dice - e.g. 8d8, 3d10, 1d10, etc.
dice = args.last("d")
newDamage = vroll(dice)

# subtract the original damage
numReroll = int(dice.split("d")[0])

# now, adjust newDamage down by the number of dice.
adjustedDamage = newDamage.total - numReroll

# collect targets
targets = args.get('t')

madeSave = args.get('saved')

c = combat()
notfound = []
impacted = []

out.append(f'-f """Meta|{newDamage} [magical fire]"""')
out.append(f'-f """Meta|{adjustedDamage} is adjustment without saves/resistances"""')

damage = f"{adjustedDamage} [magical fire]"

# It is not currently possible to correctly compute the number without needing a ton of information to be provided by the user.
# so, removing targetting for now and making the DM apply the hitpoint change themselves.
#if c and targets:
#    for target in targets:
#        who = c.get_combatant(target)
#        if who:
#            damageMessage = who.damage(damage).damage
#            out.append(f'-f """{who.name}|{damageMessage}"""')
#        else:
#            out.append(f'-f """{target}|**NOT FOUND**"""')

return " ".join(out)
</drac2>