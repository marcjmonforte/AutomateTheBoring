#This program counts how many team each character is used, not how many characters there are.

import pprint

message = raw_input('Type a message: ')
count = {} #Define dictionary that'll hold all the characters.

for character in message: #Goes through each character (meaning spaces and symbols) in the message.
	count.setdefault(character, 0) #Returns the value for that character; if not, creates it at 0.
	count[character] = count[character] + 1 #Increase by 1.

pprint.pprint(count)