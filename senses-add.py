embed -desc "<drac2>
out=[]

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

  if not xl in mySenses:
    mySenses.append(xl)
    out.append(f'* Added {xl}.')

mySenses.sort()
character().set_cvar('senses',dump_json(mySenses))

return "\n".join(out)
</drac2>"  -color <color> -thumb <image> -title "Senses" -footer """!senses [add] | [remove] "[sense1]" "[sense2]" ..."""