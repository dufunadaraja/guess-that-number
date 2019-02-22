import random

def roll_dice():
    dice = random.randint(1,6)
    count =0
    print ("GAME START")
    print (dice)
    play= str(input('Do you want to play again? '))
    while play=="yes" and count<=1:
        count+=1
        dice = random.randint(1,6)
        print (dice)
        if dice ==6 :
            print ("Double six, oya roll again")
            dice = random.randint(1,6)
            print (dice)
            play= str(input('Do you want to play again? '))
        else:
            play= str(input('Do you want to play again? '))
    print("End Game, Next Player pls")

roll_dice()       
   
