# Script name: 12timestable.py
# Purpose: prints out the multiplication table 12X12
# Author: Ogunsanya Louis Similoluwa 236345


num_1 = 1
largest_res = len(str(12 * 12)) #gets the length of the largest result
while num_1 <= 12:
    num_2 = 1
    while num_2 <= 12:
        result = num_1 * num_2 #calculates the result
        '''Gets the lenght of each result and prints 
            the appropriate amount of space before each result'''
        '''Adding 'end ='' ' at the end of the print statement ensures that
            the next print statement continues on the same line'''
        smallest_res = len(str(result))
        print(' ' * (largest_res - smallest_res), end = ' ')
        print(result, end = ' ')
        print('|', end = '')
        num_2 += 1 
    print('\n') #starts the next iteration on a new line
    num_1 += 1 
