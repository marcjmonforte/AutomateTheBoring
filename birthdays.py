birthdays = {
	'dad' : 'June 1',
	'mom' : 'May 13',
	'brother1' : 'April 12',
	'brother2' : 'July 26',
	'me' : 'August 11'}

while True:
	print('Enter a name: (blank to quit) ')
	name = raw_input()
	if name == '':
		break

	if name.lower() in birthdays:
		print(birthdays[name] + ' is the birthday for ' + name.capitalize() + '.')
	else:
		print('I do not have birthay information for ' + name.capitalize() + '.')
		print('When is their birthday?')
		bday = raw_input()
		birthdays[name] = bday
		print('Birthday database updated.')

#Doesn't add new information correctly (i.e. 'Heidi' vs 'heidi' vs 'HEIDI')