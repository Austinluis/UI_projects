# Script name: even_or_odd.py
# Purpose: checks if a number is even or odd
# Author: Ogunsanya Louis Similoluwa 236345

# function to check if the number is odd or even
def even_or_odd(n):
    print("The number is even" if n % 2 == 0 else "The number is odd")

# asks user for input
num = int(input("Enter the number: "))
# calls function       
even_or_odd(num)