#! python3
# beaconHunter.py - Finds all the beacons on the clipboard.

import pyperclip, re

# Create beacon regex
beaconRegex = re.compile(r'''(
	(\w{8})								# finds 'rubicon'
	(.)									# dot
	(\w{3})								# finds 'com'
	(/)									# dot
	(\w{6})								# finds 'beacon'
	(/)									# forward-slash
	(\w{1})								# finds 'd'
	(/)									# forward-slash
	(\w{8})								# finds first eight digits
	(-)									# separator
	(\w{4})								# finds second group of digits
	(-)									# separator
	(\w{4})								# finds third group of digits
	(-)									# separator
	(\w{4})								# finds fourth group of digits
	(-)									# separator
	(\w{12})							# finds last twelve digits
	)''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())

matches = []

for groups in beaconRegex.findall(text):
	beacons = '-'.join([groups[9],groups[11],groups[13],groups[15],groups[17]])
	matches.append(beacons)

#  Copy results to the clipboard.
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to the clipboard:')
	print('\n'.join(matches))
else:
	print('No beacons found.')