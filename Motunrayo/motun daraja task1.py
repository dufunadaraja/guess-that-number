import random
num = random.randint(1, 99)
Greeting= input("Hello, Good morning, let's start a game. To get started, click Enter")
guess = int(input("Enter an integer from 1 to 99: "))
while num!="guess":
    if guess < num:
        print ("aww! You missed it, Try again")
        guess = int(input("Enter an integer from 1 to 99: "))
    elif guess > num:
        print ("Keep trying, you are closer than you think!")
        guess = int(input("Enter an integer from 1 to 99: "))
    else:
        print ("Wow, You got it! congratulations")
        break
    
