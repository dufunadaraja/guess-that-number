import random
num = random.randint(1, 10)
guess = int(input("pick a number: "))
while (guess != num):
        print ("Try again") 
        if (guess > num):
            print ("You are far from here")
            guess = int(input("pick a number: "))
        elif (guess < num):
            print ("You are nearby")
            guess = int(input("pick a number: "))
if (guess == num):
        print ("You guessed right")
        
        
