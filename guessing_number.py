# this is a guess the number game
import random

print("Hello what is your name? ")
name = input()

print("Well, "+name+", I am thinking of a number between 1 and 20")
secretNumber = random.randint(1, 20)

attempts = 6
for guessesTaken in range(1, 7):
    try:
        if attempts == 6:
            message = "Take a guess, you have " + str(attempts) + " attempts."
        elif attempts > 1:
            message = "Try again, you have "+str(attempts)+" attempts remaining."
        else:
            message = "Your last attempt."

        print(message)
        guess = int(input())
        if guess < secretNumber:
            print("Your guess is too low\n")
            attempts -= 1
        elif guess > secretNumber:
            print("Your guess is too high\n")
            attempts -= 1
        else:
            break  # this condition is for the right guess
    except:
        print("You didn't enter a number\n")

if guess == secretNumber:
    print("Good job "+name+"! You guessed my number in " +
          str(guessesTaken)+" guesses")
else:
    print("Nope. The number I was thingking of was "+str(secretNumber))
