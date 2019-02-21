import random

def dice_roll():
    print("Your number is: " + str(random.randint(1,6)))
    play_again = input("Would you like to play again? ").lower()

    if play_again == "yes":
            dice_roll()
    elif play_again == 6:
            print("Your number is: " + str(random.randint(1,6)))
    else:
            print("Game over!")
    
dice_roll()
