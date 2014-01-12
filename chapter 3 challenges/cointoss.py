# coin toss program

import random
tosses = 0
heads = 0
tails = 0

while tosses <= 99:
        flip = random.randint(0,1)

        if flip == 0:
                heads += 1
                tosses += 1

        if flip == 1:
                tails += 1
                tosses += 1



print("You flipped the coin 100 times and got ", heads, " heads and ", tails, " tails")
