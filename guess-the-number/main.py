#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

def getNo():
    return random.randint(1,100)

def guessTheNo():
    print("Welcome to Guess the Number Game")
    print("chose between 1 to 100")
    difficulty = input("choose difficulty, type 'easy' or hard: ").lower()
    choice = 0

    if difficulty == "easy" or difficulty == "e":
        choice = 10
    else:
        choice = 5

    actualNum = getNo()
    print(actualNum)
    while choice > 0:
        print(f"you have {choice} attempt remaining, guess the number ")
        num = int(input("Make a Guess: "))

        if num < actualNum:
            print("Too Low\nGuess again")
        elif num > actualNum:
            print("Too High\nGuess again")
        else:
            print("Thats correct")
            choice = -1

        choice -= 1

    if choice == 0:
        print("all attempts exhausted")
guessTheNo()