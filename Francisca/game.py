import random
numberofGuesses = 0
number = random.randint(1,100)
name = raw_input("Hello! Who are you? ")
print (name + ", I have random numbers between 1 to 100. Can you guess what number it is?")
while numberofGuesses < 10:
    guess = raw_input("Take a guess")
    guess = int(guess)
    numberofGuesses += 1;
    guessesLeft = 10 - numberofGuesses;
    if guess < number:
        guessesLeft = str(guessesLeft)
        print("Your guess is close, you can do better! You have " + guessesLeft + " guesses Left")
    if guess > number:
        guessesLeft = str(guessesLeft)
        print("Your guess is way too high! You have " + guessesLeft + " guesses Left")

#if guess == number:
    #break
    if guess == number:
        numberofGuesses = str(numberofGuesses)
        print ("Well done! You guessed the number correctly in " + numberofGuesses + " tries")
        break
    #if guess!= number:
        #number = str(number)
        #print("Sorry. The number I was thinking " + number)


