# Script name: cal.py
# Purpose: Implements a simple calculator
# Author: Ogunsanya Louis Similoluwa 236345

def operation(num_1, operator):
    print("\n")
    global num1
    num_2 = float(input("Enter the next number: "))
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
    print("Operation:", num_1, operator, num_2)
    print("Ans: ", result)
    num1 = result
    menu(num1)

def menu(num1):
    # prompts user for type of operator
    print("-" * 20)
    print("Enter operator")
    print("Enter 1 to start again")
    print("Enter 0 to exit")
    operator = input(":")
    print("-" * 20)

    if operator == "0":
        print("Exited")
        exit
    elif operator == "1":
        print("\n")
        main()
    elif operator in "-+*/%":
        operation(num1, operator)

def main():
    num1 = float(input("Enter the first number: "))
    menu(num1)

main()