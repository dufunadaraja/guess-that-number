import random

def shomo_agemini():
    play = random.randint(1, 50)
    print("oya guess my age: ")
    print (play)
    count = 1
    var = str(input("is this your age? reply with a yes or no: "))
    a= int(input("Give me your age range, The minimum range is: "))
    b= int(input("The maximum range is: "))
    while var == "no":
       print ("ok, here is another guess")
       play = random.randint(a, b)
       print (play)
       count += 1
       var= str(input("is this your age? "))
       if(var == "yes"):
           break    
    print ("You are correct, this is my age")
    print ("number of timmes you guessed my age ", count )
shomo_agemini()
