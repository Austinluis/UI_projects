# Script name: guess.py
# Purpose: prompts user to enter a number
# And checks if he number is greater then less than or equal to a randomly generated number
# Author: Ogunsanya Louis 236345

# imports random module
import random

# assigns a random number to the variable
ran1 = random.randint(1, 100)

while True:
    # prompts user for number
    guess=int(input("Enter your lucky number from 1 to 100: "))
    # if user number is lesser than random number
    if guess < ran1:
        print("Your number is lesser try again")
    # if user number is greater
    elif guess > ran1:
        print("Your number is more try again")
    # if user number is eqaul to random number
    else:
        print("Eureka")
        break
