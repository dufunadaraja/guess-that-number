import random
random.randint(1,6)
greeting= input("Hey, will you like to roll this dice again?")
repeat="yes" or "y"
while repeat=="yes" or "y":
    print ("rolling the dice now...please wait!")
    print (random.randint(1,6))
    greeting= input("Hey, will you like to roll this dice again?")
if greeting:
    print (repeat)
    print ("rolling the dice now...please wait!")
    print (random.randint(1,6))