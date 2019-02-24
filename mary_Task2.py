# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 20:12:27 2019

@author: Mary
"""     
import random  
print ("Welcome to Rolling Game, have fun")
game_start = input(" Would you like to roll the dice?")
def roll_Dice():
   num = random.randint(1, 6)
   print("your number is: " + str(num))
   global roll_Again 
   roll_Again= input("Would you like to roll again?")
   
print ("Game Start, Rolling the Dice.........") 
roll_Dice() 

if roll_Again == "yes":
        roll_Dice()
        while roll_Again == "yes":
            roll_Dice()
elif roll_Again == "no":
        print("Game Over")
else:
        print("input not recognised!!")
        
        
    

   
    