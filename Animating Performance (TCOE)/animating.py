multiline
<drac2>
#Discord: @SylvieTG
#If it's broke, DM me or leave an issue at my GitHub repository:
#https://github.com/sylvie-spiral/AvraeStuff

using(
    nameLib = "e38598a0-1678-496c-b816-664be45c6a98"
)

ch = character()
out = []

ccUse = "Animating Performance: Animate"
ccHP = "Animating Performance: Dancing Item"
attackName = "Force Empowered Slam (object)"
creatureName = "Dancing Item"
desc = f"""As an action, you can target a Large or smaller nonmagical item you can see within 30 ft. of you and animate it. The animate item uses the Dancing Item stat block, which uses your proficiency bonus ({ch.stats.prof_bonus}). The item is friendly to you and your companions and obeys your commands. It lives for 1 hour, until it is reduced to 0 hit points, or until you die."""
help = f"{ctx.prefix}animating [-i] [-l #] - @SylvieTG"
note = "Condition Immunities charmed, exhaustion, poisoned, frightened | Darkvision 60 ft., passive Perception 10 | Speed 30 ft., fly 30 ft. (hover) | Immutable Form. | Irrepressible Dance (within 10' at start of turn, +10/-10 movement, my choice)."
ignoredUses = False
usedSpell = False

charPrefix = ch.name[0:2].upper()
groupName = nameLib.createGroupName()
itemName = f"{charPrefix}-Dancing Item"

parsedArgs = argparse("&*&")
spellSlot = parsedArgs.last("l", 0, int)

subc = "nope"
bardLevel = ch.levels.get("Bard")
isCreation = False

#no subclass until 3 for bard
if (bardLevel >= 3):
  if ("subclass" in ch.cvars):
    subc = load_json(ch.cvars["subclass"]).get("BardLevel","")
  else:
    subc = "unspecified"

  if subc == "Creation":
    isCreation = True
else:
  subc = "nope"

hasCounters = False

if (bardLevel < 6):
   #user is not high enough yet.
   desc = f"""{name} is not a 6th level bard."""   
elif not isCreation:
   #user either needs !level Bard Creation or isn't one
  desc = f"""{name} is not College of Creation (maybe `!level Bard Creation`?)."""
elif not (ch.cc_exists(ccUse) and ch.cc_exists(ccHP)):
  #user needs to setup counters
  desc = f""""Use !import, !level and !update as appropriate to create your counters. Did not find all the Creation Bard counters."""
else:
  hasCounters = True
  isAvailable = ch.get_cc(ccUse)

  if spellSlot >= 3:
    if ch.spellbook.get_slots(spellSlot):
      ch.spellbook.use_slot(spellSlot)    
      isAvailable = 1
      usedSpell = True
    else:
      desc = f"""You have no {spellSlot} spells left."""
  elif parsedArgs.last("i"):
    isAvailable = 1    
    ignoredUses = True
  elif isAvailable:
    ch.mod_cc(ccUse, -1)

  #at this point, we've either modified the counter down or opted to use a level 6 or higher spell slot if isAvailable.
  if not isAvailable:
    desc = f"""{name} tried to use animating performance, but is out of uses. Use -i if you're entering initiative with nee already created or -l # if you need to use a spell slot."""
  else:
    #Is there a combat?
    com = combat()
    if (com):
      #continue if the player is in combat
      if (com.me):
        com.me.set_group(groupName)
        #cmd = f"""{ctx.prefix}i madd "{creatureName}" -group "{groupName}" -hp {ch.cc(ccHP).max} -c "{ch.name}" -note "{note}" -h"""
        user = ctx.author.name
        cmd = f"""{ctx.prefix}i add 0 "{itemName}" -ac 16 -hp {10+(5*bardLevel)} -pb {proficiencyBonus} -strength 18 -dexterity 14 -constituion 16 -intelligence 4 -wisdom 10 -charisma 6 -immune poison -immune psychic -cr {proficiencyBonus} -type construct -note "Immune to Charmed, exhaustion, poisoned, frightened, spells/effects that alter form. 60' darkvision, immutable form. When any creature starts the turn within 10', the walking speed is increased or decreased (your choice) by 10 feet." -controller {user} -group {groupName}"""
        out.append(cmd)

        cmd = f"""{ctx.prefix}i effect "{itemName}" "Force-Empowered Slam" -attack "{ch.spellbook.sab}|1d10+{proficiencyBonus}[magical force]|{itemName} performs a Force Empowered Slam!" """
        out.append(cmd)

usesMessage = ""

if hasCounters:
  if usedSpell:
    usesMessage = f""" "Remaining level {spellSlot} Spells|{ch.spellbook.slots_str(spellSlot)}" """
  elif hasCounters:
    usesMessage = f""" "{ccUse}"|"{ch.cc(ccUse).full_str()}" """

if usesMessage != "":
  out.append(f"""{ctx.prefix}embed -footer "{help}" -title "{name} is using Animating Performance (College of Creation Bard)" -desc "{desc}" -f {usesMessage} """)
else:
  out.append(f"""{ctx.prefix}embed -footer "{help}" -title "{name} is using Animating Performance (College of Creation Bard)" -desc "{desc}" """)

return "\n".join(out)
</drac2>