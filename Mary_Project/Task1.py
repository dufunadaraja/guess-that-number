import random
num = random.randint(1, 99)
guess = int(raw_input("Enter an integer from 1 to 99: "))
while guess != num:
    print
    if guess<num:
        print "aww! You missed it, Try again"
        guess = int(raw_input("Enter an integer from 1 to 99: "))
    elif guess>num:
        print "Keep Trying "
        guess = int(raw_input("Enter an integer from 1 to 99: "))
    else:
        print "Wow, You got it!"