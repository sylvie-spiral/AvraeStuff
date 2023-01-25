# Group Name Lib
# see https://github.com/sylvie-spiral/AvraeStuff
# Purpose: generate a unique group name even if all the players shove the word professor in front of their names.

def createGroupName(prefix='',suffix='Group') -> string:
    c,ch=combat(),character()

    #if there's no combat, then just exit
    if not c or (not c.me):
        return ''

    #if I'm already in a group, then we reuse that group - unless prefix is specified
    if c.me.group and not prefix:
        return c.me.group

    # ok, lets do this: string.split(' ')
    if prefix == '':
        prefix = getInitials(ch.name)

    # proposed group name
    grpNum = 1
    grp = f'{prefix}-{suffix}{grpNum}'

    groupNames = [g.name.lower() for g in c.groups]

    if grp.lower() in groupNames:
        while grp.lower() in groupNames:
            grpNum += 1
            grp = f'{prefix}-{suffix}{grpNum}'

    return grp

def createGroupNameTarget(combatant, prefix='',suffix='Group') -> string:
    c,ch=combat(),character()

    #if there's no combat, then just exit
    if not combatant:
        return ''

    #if I'm already in a group, then we reuse that group
    if combatant.group:
        return combatant.group

    # ok, lets do this: string.split(' ')
    if prefix == '':
        prefix = getInitials(ch.name)

    # proposed group name
    grpNum = 1
    grp = f'{prefix}-{suffix}{grpNum}'

    groupNames = [g.name.lower() for g in c.groups]

    if grp.lower() in groupNames:
        while grp.lower() in groupNames:
            grpNum += 1
            grp = f'{prefix}-{suffix}{grpNum}'

    return grp

def getInitials(name) -> string:
    prefix = ''

    parts = name.split(' ')
    for part in parts:
        p = part[0:1]
        if p.isalpha():
            prefix += part[0:1]

    if '' == prefix:
        prefix = name[0:2]

    return prefix

#tested with: Elena "d'tester" Voidspark
#returns:     Elena \"d\'tester\" Voidspark
#which then should be OK for embed fields, etc.
def getSafeName(name) -> string:
    if not name:
        return ""
    
    # ok, we have a name
    temp = name

    temp = temp.replace("'","\\\\'")

    return temp
