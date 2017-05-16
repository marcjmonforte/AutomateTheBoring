theBoard = {'top-L':' ','top-M':' ','top-R':' ',
			'middle-L':' ','middle-M':' ','middle-R':' ',
			'bottom-L':' ','bottom-M':' ','bottom-R':' '}

def printBoard(board):
	print(board['top-L'] + "|" + board['top-M'] + "|" + board['top-R'])
	print('-+-+-')
	print(board['middle-L'] + "|" + board['middle-M'] + "|" + board['middle-R'])
	print('-+-+-')
	print(board['bottom-L'] + "|" + board['bottom-M'] + "|" + board['bottom-R'])

turn = 'X'
for i in range(9):
	printBoard(theBoard)
	move = raw_input('Turn for ' + turn + ". Move on which space? ")
	theBoard[move] = turn
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'
printBoard(theBoard)

#It doesn't replace the value though...