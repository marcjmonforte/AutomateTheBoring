#! /usr/bin/env python3
# bulletPointAdder.py - Takes a list and adds bullet points to each line.

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)) :	#loop through all indexes in the "lines" list
	lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)