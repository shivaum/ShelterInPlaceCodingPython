# key: value
# '1': '1' 
# '2': '2'
# '3': '3'
# ...
# '5': '5' -> '5': 'X'
theBoard = {}

board_keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for key in board_keys:
	theBoard[key] = key

def printBoard(board):
	print(board['1'] + '|' + board['2'] + '|' + board['3'])
	print('-----')
	print(board['4'] + '|' + board['5'] + '|' + board['6'])
	print('-----')
	print(board['7'] + '|' + board['8'] + '|' + board['9'])

def checkWin(board, turn):
	# across the top
	if board['1'] == board['2'] == board['3']:
		printBoard(board)
		print("\nGame Over!\n")
		print(turn + " has won!")
		return True
	# across the middle
	elif board['4'] == board['5'] == board['6']:
		printBoard(board)
		print("\nGame Over!\n")
		print(turn + " has won!")
		return True
	# accros the bottom
	elif board['7'] == board['8'] == board['9']:
		printBoard(board)
		print("\nGame Over!\n")
		print(turn + " has won!")
		return True
	# down the left side
	elif board['1'] == board['4'] == board['7']:
		printBoard(board)
		print("\nGame Over!\n")
		print(turn + " has won!")
		return True
	# down the middle
	elif board['2'] == board['5'] == board['8']:
		printBoard(board)
		print("\nGame Over!\n")
		print(turn + " has won!")
		return True
	# down the right side
	elif board['3'] == board['6'] == board['9']:
		printBoard(board)
		print("\nGame Over!\n")
		print(turn + " has won!")
		return True
	# left diagonal
	elif board['1'] == board['5'] == board['9']:
		printBoard(board)
		print("\nGame Over!\n")
		print(turn + " has won!")
		return True
	# right diagonal 
	elif board['3'] == board['5'] == board['7']:
		printBoard(board)
		print("\nGame Over!\n")
		print(turn + " has won!")
		return True
	return False

def game():
	turn = 'X'
	num_moves = 0

	while True:
		printBoard(theBoard)
		print("It is your turn " + turn)
		move = input("Where would you like to place your " + turn + "\n")

		try:
			checkMove = (theBoard[move] == str(move))
		except KeyError:
			print("Invalid input, please try again")
			continue

		if checkMove:
			theBoard[move] = turn
			num_moves += 1
		else:
			print("That place has already been filled.\n")
			continue

		if checkWin(theBoard, turn):
			break

		if num_moves == 9:
			printBoard(theBoard)
			print("\nGame Over!\n")
			print("There was a tie!")
			break

		if turn != 'X':
			turn = 'X'
		else:
			turn = 'O'

	restart = input("Do you want to play again?(y/n)\n")
	if restart == 'y' or restart == 'Y':
		for key in board_keys:
			theBoard[key] = key
		game()

game()
