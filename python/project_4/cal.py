# Script name: cal.py
# Purpose: Implements a simple calculator
# Author: Ogunsanya Louis Similoluwa 236345

# function to convert the input to either int of float based on input
def input_type(input):
    '''converts the input to int and if it raises a value error
       it converts it to a float'''
    try:
        input_value = int(input)
    except ValueError:
        input_value = float(input)
    return input_value #returns the converted value

# this function carries out the operation and prints out the result
def operation(num_1, operator):
    print("\n")
    num_2 = input("Enter the next number: ") #asks for the next number
    num_2 = input_type(num_2) #converts the input to the appripriate type
    # Operations
    if operator == "+":
        result = num_1 + num_2
    elif operator == "-":
        result = num_1 - num_2
    elif operator == "*":
        result = num_1 * num_2
    elif operator == "/":
        result = num_1 / num_2
    elif operator == "%":
        result = num_1 % num_2
    print("\n")
    print("-" * 20)
    # prints the result
    print("Operation:", num_1, operator, num_2)
    print("Ans: ", result)
    num1 = result
    # calls the menu function if user wants to calculate along with the result
    menu(num1)

# menu function contains code to ask user for the operator and for exiting
def menu(num1):
    # prompts user for type of operator
    print("-" * 20)
    print("Enter operator")
    print("Enter 1 to start again")
    print("Enter 0 to exit")
    operator = input(":")
    print("-" * 20)

    # ends the program
    if operator == "0":
        print("Exited")
        exit
    # starts the calculation from scratch refreshing the value of the result
    elif operator == "1":
        print("\n")
        main()
    # calls the operation function to carry out the calculations
    elif operator in "-+*/%":
        operation(num1, operator)

# main function
def main():
    num1 = input("Enter the first number: ") #asks user to input the first number
    num1 = input_type(num1) #converts the number to its appropriate type
    menu(num1)

# calls main funtion to start the code
main()