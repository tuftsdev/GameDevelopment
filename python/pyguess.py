# Last updated on July 18, 2010
from random import randint

min = 1
max = 100
secret = randint(min, max)
print("Welcome!")
guess = 0
numGuesses = 0
while guess != secret:
	guess = 0
	while guess < min or guess > max:
		g = input("Guess the number between " + str(min) + " and " + str(max) + " (inclusive): ")
		guess = int(g)
		if guess < min or guess > max:
			print "You bozo, your guess does not count.  Try again."
	numGuesses = numGuesses + 1 # Anything interesting?
	if guess == secret:
		print("You win!  It took you " + str(numGuesses) + " guesses.")
	else:
		if guess > secret:
			print("Too high")
		else:
			print("Too low")
print("Game over!")
