import random

def dice_roll():
    random_no = random.randint(1,6)
    print("Your number is: " + str(random_no))
    while random_no == 6:
        random_no = random.randint(1, 6)
        print("Double six: " + str(random_no))
        #dice_roll()
    play_again = input("Would you like to play again? ").lower()

    if play_again == "yes":
        dice_roll()
    else:
        print("Game over!")
    
dice_roll()
