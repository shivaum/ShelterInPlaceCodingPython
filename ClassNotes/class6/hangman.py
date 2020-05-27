print("Welcome to Hangman")

word = "python is fun"

# python is fun
# ------ -- ---

total_guesses = 10

guesses = ""

while total_guesses > 0:
	not_guessed = 0

	for char in word:
		if char in guesses:
			print(char, end='')
		elif char == ' ':
			print(' ', end='')
		else:
			print("-", end='')
			not_guessed += 1

	print()

	if (not_guessed == 0):
		print("You have guessed the word!")
		break # terminates loop

	user_guess = input("Guess a letter: ")

	if (len(user_guess) > 1):
		print("Incorrect letter was given")
		continue

	if user_guess in guesses:
		print("You have already guessed this letter")
		continue # go back to top of loop

	guesses += user_guess

	if user_guess not in word:
		total_guesses -= 1
		print("Incorrect guess")
		print("You have", total_guesses, "guesses left")

if (total_guesses == 0):
	print("You lost the game. The word was", word)


