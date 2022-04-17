embed -desc "<drac2>

mySenses = get('senses')
if mySenses:
  if mySenses.find('[') == 0:
    mySenses = load_json(mySenses)
  else:
    mySenses = mySenses.split(',')  

if not mySenses:
  mySenses = []

for x in &ARGS&:
  xl = x.lower()

  if xl in mySenses:
    mySenses.remove(xl)    

mySenses.sort()
character().set_cvar('senses',dump_json(mySenses))

return mySenses
</drac2>"  -color <color> -thumb <image> -title "Senses" -footer """!senses [add] | [remove] "[sense1]" "[sense2]" ..