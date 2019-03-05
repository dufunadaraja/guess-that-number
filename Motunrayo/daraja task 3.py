import random
def my_age():
    age = 31
    guess = random.randint(24, 32)
    guess_age= str(input("Are you " + str(guess) + " years old?"))
    while guess_age == "n":  
        if guess < age:
           guess = random.randint(24, 32)
           print (guess)
           guess_age= str(input("Are you " + str(guess) + " years old?"))
        elif guess > age:
            guess = random.randint(24, 32)
            print (guess)
            guess_age= str(input("Are you " + str(guess) + " years old?"))
            break
    print ("correct age!!!")
        
    print ('game over' )
my_age()
        
