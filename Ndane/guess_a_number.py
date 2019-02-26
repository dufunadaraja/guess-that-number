"""
This is a multi line comment

that shows a random guessing game
"""
print "random guessing game starting..."

import random

guess=10 

count=0  

no = random.randint(1,10)  


print "Welcome to the guessing game!"


while guess != no :  
    guess = int(raw_input("Guess a number: ")) 

    if guess < no : 
        print("Try again") 
        count+=1  

    elif guess > no :
        print("Ouch! You missed it...") 
        count+=1  

    else :
        print("Wow that's great that was the number indeed:",no)
        print("It took you a total of:",count,"tries")
