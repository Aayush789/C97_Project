import random

print("Number Guessing Game between 1-10")

chances= 5

randomNumber= random.randint(1,10)

while chances>0:

    guessingNumber= int(input("enter your guessingNumber: "))

    if (guessingNumber<randomNumber):
        print("Your Guess was too low: Guess a higher number")
    elif(guessingNumber==randomNumber):
        print("Congratulation you Won")
        break
    else:
        print("Your Guess was too high: Guess a lower number")

    chances= chances-1
if not chances>0:
    print("You Lose. The number is ", randomNumber)
    