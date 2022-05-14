<drac2>
ect = "Eldritch Claw Tattoo"
key = f'{ect}-{name}'

if not combat():
  return ""

t = floor(time())
last = floor(combat().get_metadata(key, 0))

if t - last > 0:
  combat().set_metadata(key, str(t))
  return f"-f 'Once|Just one time' -f '{t}|{last}'"
else:
  return "-f 'Nope|Already Run'"

return output
</drac2>