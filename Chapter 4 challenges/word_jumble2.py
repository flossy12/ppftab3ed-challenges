import random


WORD_HINT = [
("apple", "The wicked witch gives snow white one"),
("submarine", "The Beatles sang about a yellow one"),
("xylophone", "patrick moore plays one"),
("Archer", "an egotistical spy who loves top gun")]

pair = random.choice(WORD_HINT)
word = pair[0]
hint = pair[1]
correct = word

jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]

print("""
	\t\twelcome to word jumble!\n
	\tUnscramble the letters and guess the word to win\n
	\n\t\tYou can ask for a hint by pressing '?'\n
	\tYou score 10 points for solving the jumble without a hint,
	\tbut only 5 in you take the hint\n
	\n\t\tPress the enter key to quit the game....\n""")

print("Your current jumble is: ", jumble,"\n")

guess = input("Take a guess! you can hit enter to quit or ? to get a hint: ")

score = 10

while guess != correct and guess != "" and guess !="?":
	print("\nSorry, that's not right.")
	guess = input("\nTake a guess! Enter to quit or ? for a hint: ")

	if guess == correct:
		print("You nailed it! You got the right answer!")

	elif guess == "?":
		score = 5
		print(hint)
		guess = input("\nTake a guess! Enter to quit or ? for a hint: ")

print("thanks for playing! You scored ", score, " points")
input("\n press enter to exit...")
