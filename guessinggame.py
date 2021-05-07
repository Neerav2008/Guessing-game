import random
 
#constants for random nuneber and number of tries the user takes
random_number = random.randint(1,9)
tries = 1

#user interaction
username = input("Hi, I am bored, what's your name? ")
 
print("Hello", username+",", )

#choice to play game
question = input("I am bored, so let's play a number guessing game. [Y/N] ")

#if the user denies to play the game 
if question == "n":
    print("fine...your bad, I will just find someone else to play a game with..")
 
#if a usr agrees
if question == "y":
    print("Then. guess a number between 1 and 9")
    guess = int(input("Go on, have a guess :"))
    if guess > random_number:
        print("Guess Lower...")
    if guess < random_number:
        print("Guess Higher...")
 
    while guess != random_number:
        tries += 1
        guess = int(input("Try Again : "))
        if guess <random_number:
            print("Guess Higher...")
    if guess == random_number:
        print("Congratulations, the number was", random_number,"and you guessed it right in only", tries,"tries!")
#End message for congratulations
 
