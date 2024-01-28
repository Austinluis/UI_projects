# Script Name: rad.py
# Purpose: A program to convert a number from radians to degree
# Author: Ogunsanya Louis Similoluwa 236345

# while loop to ensure program continuity
while True:
    # asks for input
    rad = input("Enter the angle in radians. Enter \"000\" to cancel: ")

    # checks if input is a numerical value
    while True:
        if rad.isdigit:
            break
        # prints an error message if input is not a numerical value
        print("INPUT ERROR: input should be a numerical value!")
        rad = input("Enter the angle in radians. Enter \"000\" to cancel: ")

    # exit option
    if rad == "000":
        break
    
    # converts the input to degrees
    deg = float(rad) * 180
    
    # if input is an integer
    if rad.isdigit():
        # rounds off answer to whole number
        deg = round(deg)

    # outputs the converted result
    print(rad, "radians is equal to", deg, "degrees")