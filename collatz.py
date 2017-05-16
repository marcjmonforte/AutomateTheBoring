def collatz():
	try:
		number = int(input('Please enter a number: '))
	except:
		print 'You are not listening to instructions.'
		collatz()
	else:
		while not number == 1:	#This will keep looping for as long as number does not equal "1".
			if number % 2 == 0:
				number = (number // 2)
				print number
				continue
			else:
				number = ((3 * number) +1)
				print number
				continue
		print "Collatz sequence complete."

collatz()