print "Sho mo age mi ni?"
import random
guess = 0
age = int(raw_input("write a number between 1 and 100 "))
print "computer sho mo age mi in?"

while age > 100 or age < 1:
    age = int(raw_input("Write a number between 1 and 100 "))
    
while guess != age :
    guess = random.randrange(101)
    print"Are you", guess
    past = guess
    while guess < age:
        guess = random.randrange(guess,101)
        print"Are you", guess
    while guess > age:
        guess = random.randrange(0,guess)
        print "Are you", guess
        if guess == age:
            print"Excellent, you got it"
            break

raw_input("Press enter to exit.")
            
