#Comma Code

spam = ['apples', 'bananas', 'tofu', 'cats'] #Define list

def foo(listname):
	#Need to return a string with all items separated by comma and space
	#Last item needs 'and' before it

	for i in listname:
		if not str(i) == listname[-1]:
			print i,
			print ",",
		else:
			print "and ", i

foo(spam) #Execute the function