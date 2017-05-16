#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

# Create phone regex
phoneRegex = re.compile('''(
	(\d{3}|\(\d{3}\))?					# area code, optional as notated by ?
	(\s|-|\.)?							# separator
	(\d{3})								# first 3 digits
	(\s|-|\.)							# separator
	(\d{4})								# last 4 digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))?		# extension, optional as notated by ?
	)''', re.VERBOSE)

# Create email regex
emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+					# username, comprised of any of these letters / symbols
	@									# @-symbol
	[a-zA-Z0-9.-]+						# domain name
	(\.[a-zA-Z]{2,4})					# dot-something (.com, .net)
	)''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())

matches = []

for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1],groups[3],groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + group[8]
	matches.append(phoneNum)

for groups in emailRegex.findall(text):
	matches.append(groups[0])

#  Copy results to the clipboard.
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to the clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers of email addresses found.')