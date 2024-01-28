# Script name: factorial.py
# Purpose: prints the factorial of a number
# Author: Ogunsanya Louis Similoluwa 236345

# function factorial
def factorial(num):
    # the factorial of 0 and 1 is 1
    if num <= 1:
        return 1
    # calculates the factorial of the number
    # by recursively multiplying the number by its subsequent decreaments by 1
    else:
        return (num * factorial(num - 1))

# asks user to input number
num = int(input("Enter the number: "))        
print("The factorial of", num, "is", factorial(num))