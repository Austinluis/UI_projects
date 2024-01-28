# Script name: multiply.py
# Purpose: prints out the multiplication table of a number
# Author: Ogunsanya Louis Similoluwa 236345

# function to print the multiplication table
def multiply(num):
    num_1 = 1 # first loop value and multiplication value
    largest_res = len(str(num * num)) # gets the length of the largest result
    while num_1 <= num: # while loop for multiplication
        num_2 = 1 # second loop value and multiplication value
        while num_2 <= num: # while loop for multiplication
            result = num_1 * num_2 # calculates the result
            '''Gets the lenght of each result and prints 
               the appropriate amount of space before each result'''
            '''Adding 'end ='' ' at the end of the print statement ensures that
               the next print statement continues on the same line'''
            smallest_res = len(str(result))
            print(' ' * (largest_res - smallest_res), end = ' ')
            print(result, end = ' ')
            num_2 += 1 # increaments loop 2
        print('\n') # starts the next iteration on a new line
        num_1 += 1 # increaments loop 1

number = int(input("Enter the number: ")) # asks user for number
# calls the multiply function to print the multiplication table of the number
multiply(number)