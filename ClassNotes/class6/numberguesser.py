import random

print("Welcome to Number Guesser!")

random_num = random.randint(1, 10)

max_chances = 5

user_guesses = 0

while user_guesses < max_chances:
	guess = int(input("Enter your guess: "))
	if (guess == random_num):
		print("You have guessed the number")
		break
	elif (guess < random_num):
		print("The number you have guessed is too small")
	else:
		print("The number you have guessed is too big")
	user_guesses += 1

if user_guesses >= max_chances:
	print("You have lost, the number was", random_num)