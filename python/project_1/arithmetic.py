# Script name: arithmetic.py
# Purpose: a simple calculator that takes two numbers, performs some arithmetic opererations and outputs the result assuming the positions of the numbers are not fixed
# The arithmetic operations include: addition, subtraction, multiplication, division and exponential
# Author: Ogunsanya Louis 236345

# collects input and assigns to variables
first_number = int(input("Enter the first number and press enter:"))
second_number = int(input("Enter the second number and press enter:"))

# prints a space between the input and output
print("\n")

# assigns the answer to the operations to variables
addition = first_number + second_number
subtraction1 = first_number - second_number
subtraction2 = second_number - first_number
multiplication = first_number * second_number
division1 = first_number / second_number
division2 = second_number / first_number
exponential1 = first_number ** second_number
exponential2 = second_number ** first_number

# outputs the results
print("Addition of the two numbers = ", addition)
print("Subtraction of the second number from the first number = ", subtraction1)
print("Subtraction of the first number from the second number = ", subtraction2)
print("Multiplication of the two numbers = ", multiplication)
print("Dision of the first number by the second number = ", division1)
print("Division of the second number by the first number = ", division2)
print("The first number exponential the second number = ", exponential1)
print("The second number exponential the first number = ", exponential2)
