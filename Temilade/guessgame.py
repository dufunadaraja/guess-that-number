#This code allows a user to guess a number between the range of 1 to 20
import random

number = random.randint(1,20)
guess = int(input("Enter any number: "))

while (guess != number):
    print 
    if (guess < number):
        print ("guess is low")
        guess = int(input("Enter an integer from 1 to 20: "))
    elif(guess > number):
        print ("guess is high")
        guess = int(input("Enter an integer from 1 to 20: "))
print("correct")