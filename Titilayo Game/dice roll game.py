import random
def dice_game():
  dice_roll = random.randint(1,6)
  comp_guess = 0
  print (dice_roll)
  print("Aww! you have to guess again")
  play_again= str(input("Do yo want to play again?"))
  while play_again == "y":
    dice_roll = random.randint(1,6)
    print(dice_roll)
    if dice_roll == 6:
      print("oya play again")
      dice_roll = random.randint(1,6)
      print(dice_roll)            
    elif dice_roll < 6:
      print("I'm actually looking for a six")
      play_again= str(input("Do yo want to play again?"))
  print ("Game Over")
dice_game()
