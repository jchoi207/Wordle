import sys
import random
from termcolor import colored

guesses = [["_"] * 5 for _ in range(6)]
colors = [[""] * 5 for _ in range(6)]
words = (open("words.txt", "r")).readlines()

def generate_target():
    return words[random.randint(1,14855)]

def new_line(n, guess, target):
    for i in range(5):
        guesses[n][i] = guess[i]

    for i in range(5):
        if guess[i] == target[i]:
            colors[n][i] = "green"
            colors[n][i]
        elif guess[i] in target[:5]:
            colors[n][i] = "yellow"
        else:
            colors[n][i] = "black"

def display_board(n, guess, target):
    # display the board
    new_line(n, guess, target)
    for i in range(6):
        print(str(i+1), end = " ")
        
        for j in range(5):
            if guesses[i][j] == "_":
                print("___   ___   ___   ___   ___")
                break
            else:
                text = colored(guesses[i][j], colors[i][j], attrs=["reverse", "blink"])
                print("_"+ text  + "_", end = "")
                print("   ", end = "")
        print("\n")

def start_game(): 
    target = generate_target()
    for i in range(6):
        print(str(i+1), end = " ")
        print("___   ___   ___   ___   ___")
        print("\n")
    
    n = 0 
    correct = False
    while not correct and n < 6: 
        guess = str(input("Guess a 5 letter word: "))
        if str(guess+"\n") == target or guess == target: 
            correct = True
            display_board(n, guess, target) 
            print("Correct! You guessed right in ", str(n+1) , " turns!")
            break 

        elif str(guess+"\n") in words: 
            display_board(n, guess, target) 
            n += 1 
        
        else:
            print("Enter a valid word")
    print("You lose. The word was: ", target)
start_game()

