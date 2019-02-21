import random

def roll_dice():
    dice = random.randint(1,6)
    print (dice)
   
print("Start Game")
roll_dice()
play= str(input('Do you want to play again? '))
count = 0
while play == 'yes'and count<=5:
    roll_dice()
    count+= 1
    play= str(input('Do you want to play again? '))
    if play =='no':
        print("End Game, Next Player pls")
        
    else:
        print
