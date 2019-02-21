"""
Random Number Guessing Game
"""
import random
#guess out a secret number ranging from 1 to 50
# let the user guess  be any number within or outside the number range
# so we can get started with our "while loop"
secret_number = random.randint(1, 50)
user_guess = 0

# So for the while loop, print True if guess no is correct or False if 
# wrong
if user_guess > secret_number:
    print ("True")