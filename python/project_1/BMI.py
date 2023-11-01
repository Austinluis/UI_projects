# Script name: BMI.py
# Purpose: Calculates the Body Mass Index
# Body Mass Index(BMI): BMI = weight / height * height
# Author: Ogunsanya Louis 236345

# Takes inputs and assigns it to a variable
Weight = float(input("Enter the weight in kg and press enter:"))
Height = float(input("Enter the height in meters and press enter:"))

# prints a blank line between the input and the output
print("\n")

# Calculates the BMI and assigns it to a variable
height_square = Height * Height
BMI = Weight / height_square

# Outputs the BMI
print("The Body Mass Index(BMI) = ", BMI)
