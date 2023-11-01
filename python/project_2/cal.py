# Script name: cal.py
# Purpose: Implements a simple calculator with a menu
# Author: Ogunsanya Louis 236345

# prompts user for input
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))

# prompts user for type of operator
print("Select an operation: ")
print("Add the two numbers press 0")
print("Subtract the two numbers press 1")
print("Multiply the two numbers press 2")
print("Divide the two numbers press 3")
print("Modulus of the two numbers press 4")
print("To quit press 5")

# carries out operation and outputs the result
response=input(":")

if response == "0":
    print("Your answer is: ", (num1 + num2))
elif response == "1":
    print("Your answer is: ", (num1 - num2))
elif response == "2":
    print("Your answer is: ", (num1 * num2))
elif response == "3":
    print("Your answer is: ", (num1 / num2))
elif response == "4":
    print("Your answer is: ", (num1 % num2))
elif response == "5":
    print("Quit")
