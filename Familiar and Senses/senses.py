embed
<drac2>
mySenses = get('senses')
if mySenses and len(mySenses) > 0:
  if mySenses.find('[') == 0:
    mySenses = load_json(mySenses)
  else:
    mySenses = mySenses.split(',')
else:
  mySenses = []

if len(mySenses) > 0:
  return '-desc "**Special Senses**:\n* ' + "\n* ".join(mySenses) + '"'
else:
  return "-desc 'No special senses defined.'"
</drac2> -color <color> -thumb <image> -title "Senses" -footer """!senses [add] | [remove] "[sense1]" "[sense2]" ..."""