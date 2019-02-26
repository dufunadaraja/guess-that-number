import random
guess_num = random.randint(1,50)
user_guess =input("what number did you guess?")

while (int(user_guess) != guess_num):
    print("Ouch!it's wrong")
    if(int(user_guess) > guess_num):
        print ("Guess is high")
        user_guess =input("Will you try guessing again?")
    elif(int(user_guess) < guess_num):
        print ("Guess is low")
        user_guess =input("Will you try guessing again?")
if (int(user_guess)== guess_num):
    print ("That's very correct")
    
 
