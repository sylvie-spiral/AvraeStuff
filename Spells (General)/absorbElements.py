embed <drac2>
o,ms,ch,pa,args = [],[],character(),argparse("&*&"),&ARGS&
spell_text = """The spell captures some of the incoming energy, lessening its effect on you and storing it for your next melee attack. You have resistance to the triggering damage type until the start of your next turn. Also, the first time you hit with a melee attack on your next turn, the target takes an extra 1d6 damage of the triggering type, and the spell ends."""
at_higher = """At Higher Levels|When you cast this spell using a spell slot of 2nd level or higher, the extra damage increases by 1d6 for each slot level above 1st."""

c,i,l,dt,amt = combat(),pa.last("i"),pa.last("l", 1),pa.last("dt", None),pa.last("amt")
desc = []
fields = []
dice = f"{l}d6 [magical {dt}]"

allowed_damage_types = ["fire","ice","acid","thunder","lightning"]

if (not dt) or (not amt):
    if not dt:
        desc.append(f"You must use `-dt` to specify one of {allowed_damage_types}")
    if not amt:
        desc.append(f"`-amt` to specify the damage you took.")

    desc.append(f"Example: `!absorbElements -dt fire -amt 33` if you took 33hp from a fireball.")
elif not dt.lower() in allowed_damage_types:
    desc.append(f"You can't cast this spell for {dt} damage")
    desc.append(f"Allowed damage types are: {allowed_damage_types}")
elif not (i or ch.spellbook.can_cast('Absorb Elements', l)):
    desc.append(f"You can't cast that spell right now (check your spellbook, can use `-i` to override)")
    fields.append(f"{l} level spells|{ch.spellbook.slots_str(l)}")
else:    
    if int(l) > 1:
        fields.append(at_higher)        

    desc.append(spell_text)

    # we're an allowed damage type, have an amt, and have a slot - but hold off using it for just a moment in case we error out.
    if c and c.me:
        #add the effect
        c.me.add_effect(f"Absorb Elements (Resistance)", f"-resist {dt}", duration = 1, concentration=False, parent=None, end=False, desc="You have resistance to the triggering damage type until the start of your next turn.")
        c.me.add_effect(f"Absorb Elements (Melee)|{dice}", "", duration = 2, concentration= False, parent=None, end=True, desc=f"Also, the first time you hit with a melee attack on your next turn, the target takes an extra {dice} damage of the triggering type, and the spell ends.")

        #add back the hitpoints:
        restore_amt = ceil(int(amt)/2)
        old_hp = c.me.hp
        fields.append(f"""HP mitigated|{c.me.hp_str()} + {restore_amt}""")
        c.me.modify_hp(restore_amt, False, False)        

        fields.append(f"""On your round|You can use `absorbElements` as part of your next melee attack to inflict the bonus {dt} damage.""")
    else:
        desc.append("**You are not currently in a combat and so the snippet will not work**")

    if i:
        fields.append("Ignore Spell Slot|User specified to ignore requirements.")
    else:
        ch.spellbook.use_slot(l)
        fields.append(f"Reamining {l} Spells|{ch.spellbook.slots_str(l)}")

final_desc = "\n".join(desc)

o.append(f'-desc "{final_desc}"')

for f in fields:
    o.append(f' -f "{f}" ')

return " ".join(o)

</drac2> -title '<name> casts Absorb Elements!' -footer "!absorbElements <-a #> <-dt damage type>" -thumb <image> -color <color>