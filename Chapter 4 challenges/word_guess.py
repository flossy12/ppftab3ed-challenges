import random

wordlist = ("criminal", "martini", "spaceship", "moon", "chicken", "present", "coffee", "bridge")

word = random.choice(wordlist)
length = len(word)
correct = word
guessedLetters = ""

print("Your word is ", length, " letters long\n")
guess = ""

for i in range(5):
	guess = input("guess a letter in the word: ")
	
	if guess in word:
		print("yes, that letter is in the word!\n")
		guessedLetters += guess
		print("the letters you've guessed right so far are: ", guessedLetters)

	else:
		print("too bad, that letter isn't there!\n")
		print("the letters you've guessed right so far are: ", guessedLetters)

lastguess = input("you've had your 5 guesses, now guess the word: ")
if lastguess == correct:
	print("you guessed right!!")

else:
	print("sorry that's not it - you lose!!")
