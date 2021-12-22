multiline
<drac2>
#Discord: @SylvieTG#4737
#If it's broke, DM me or leave an issue at my GitHub repository:
#https://github.com/sylvie-spiral/AvraeStuff
#Needs Dancing Item in your bestiary (I used https://critterdb.com/#/publishedbestiary/view/5fc08281f9101e03eeb5333e)
ch = character()
out = []

ccUse = "Animating Performance: Animate"
ccHP = "Animating Performance: Dancing Item"
attackName = "Force Empowered Slam (object)"
creatureName = "Dancing Item"
desc = f"""As an action, you can target a Large or smaller nonmagical item you can see within 30 ft. of you and animate it. The animate item uses the Dancing Item stat block, which uses your proficiency bonus ({ch.stats.prof_bonus}). The item is friendly to you and your companions and obeys your commands. It lives for 1 hour, until it is reduced to 0 hit points, or until you die."""
help = "!animating [-i] [-l #] - @SylvieTG#4737"
note = "Condition Immunities charmed, exhaustion, poisoned, frightened | Darkvision 60 ft., passive Perception 10 | Speed 30 ft., fly 30 ft. (hover) | Immutable Form. | Irrepressible Dance (within 10' at start of turn, +10/-10 movement, my choice)."
ignoredUses = False
usedSpell = False

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
        groupName = "AP-" + com.me.name
        com.me.set_group(groupName)
        cmd = f"""{ctx.prefix}i madd "{creatureName}" -group "{groupName}" -hp {ch.cc(ccHP).max} -c "{ch.name}" -note "{note}" -h"""
       
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