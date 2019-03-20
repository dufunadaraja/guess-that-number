# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 11:09:10 2019

@author: Mary
"""

import random
print ("How old are you?")
def age_Guess():
    age_range=[18,25,27,29,30,32,35,39]
    global myGuess
    myGuess = (age_range[random.randint(0, len(age_range) - 1)])
print ("Are you" , myGuess ,"Years Old?")   
age = input("Enter your answer: ")
if age == "less":
        age_Guess()
elif age == "more":
        age_Guess
else:
        print("correct")
        while age != "correct":
            age_Guess()
        