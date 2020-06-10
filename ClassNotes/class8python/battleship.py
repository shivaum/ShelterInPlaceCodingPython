# https://codingbat.com/python
# https://leetcode.com/problemset/all/?difficulty=Easy

from random import randint

# initialize a board
board = []

for i in range(5):
	board.append(["O"] * 5)

# print(board)

def print_board(board):
	for arr in board:
		# print(arr)
		print(" ".join(arr))

print("Let's play Battleship!")
print("Rows are numbered from 0-4. The top row is Row 0 and the bottom row is Row 4.\n")
print("Columns are numbered from 0-4. The left column is Column 0 and the rightmost column is Column 4.\n")
print("You have 4 turns to guess the ship location\n")

print_board(board)


ship_row = randint(0, len(board) - 1)

ship_col = randint(0, len(board[0]) - 1)

turn = 0

while True:
	try:
		guess_row = int(input("Guess Row: "))
		guess_col = int(input("Guess Column: "))
	except ValueError:
		print("Invalid input row/col. Please try again...")
		continue

	if (guess_row == ship_row) and (guess_col == ship_col):
		print("Congratulations! You sunk my battleship")
		break
	else:
		# edges cases
		if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
			print("Your input was outside of the board")
			continue
		elif (board[guess_row][guess_col] == "X"):
			print("You have already guessed this spot.")
			continue
		else:
			print("You missed my battleship!")
			board[guess_row][guess_col] = "X"

		turn += 1

		print("Turn " + str(turn) + " out of 4.")
		print_board(board)

		if turn > 3:
			print("Game Over")
			print("The ship was at row " + str(ship_row) + " and the column was at " + str(ship_col))
			board[ship_row][ship_col] = "1"
			print_board(board)
			break


