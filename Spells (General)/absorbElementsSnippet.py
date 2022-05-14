<drac2>
# use absorb elements
if not combat():
    return "-f 'Absorb Elements|You are not currently in combat so you will need to apply this manually.'"
else:
    ef = combat().me.get_effect("Absorb Elements (Melee)")
    if not ef:
        return "-f 'Absorb Elements|Did not find the Absorb Elements effect.'"
    else:
        dice = ef.name.split("|")[1]
        return f'-d "{dice}" -f "Absorb Elements|Also, the first time you hit with a melee attack on your next turn, the target takes an extra {dice} damage of the triggering type, and the spell ends."'
</drac2>