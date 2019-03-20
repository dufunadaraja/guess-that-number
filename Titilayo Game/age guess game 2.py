import random
def age_game():
  My_age= random.randint(30,35)
  comp_guess = 0
  print ("What is your age?")
  age_guess= str(input("Do yo want to play age guess?"))
  while age_guess == "yes":
    My_age= random.randint(30,35)   
    print(My_age)
    if My_age >31:
      print("That is not my age")
      print("Guess too high")         
    elif My_age< 31:
     print("That is not my age")
     print("Guess too low")
     My_age = random.randint(30,35)
     print(My_age)
    elif My_age==31:
      print("That's my actual age,you are correct")
      age_guess= str(input("Do yo want to play again?"))
  print ("Game Over")
age_game()
