import random

highnumber = 101
lownumber = 1
guess = random.randrange(lownumber,highnumber)
won = False


print("welcome to the guess a number game! Pick a number between 1 & 100 \n")
print("my first guess is: ",guess)

while won != True:
    userinput = input("Higher, Lower or Got It? \n")
    
    if userinput == "higher":
        lownumber = guess
        guess = random.randrange(lownumber, highnumber)
        print("my next guess is: ",guess)
        
    elif userinput == "lower":
        highnumber = guess
        guess = random.randrange(lownumber, highnumber)
        print("my next guess is: ",guess)
        
    elif userinput == "got it":
        print("I guessed right! Your number was",guess)
        won = True
