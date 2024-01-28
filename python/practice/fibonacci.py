# Script name: fibonacci.py
# Purpose: prints the nth fibonacci number
# Author: Ogunsanya Louis Similoluwa, 236345

''' Asumptions: in this code it is assumed that 0 is the ground/0th term of 
    the fibonacci sequence and 1 is the fist term i.e '0,1,1,2,3,5..' '''

# function fibonacci to find the nth fibonacci number
# nth_number: the fibonacci number to be printed
def fibonacci(nth_number):
    # declaring variables
    # start variable for while loop iteration
    start = 0
    # ground_term and first_term variables for 0 and 1
    ground_term = 0
    first_term = 1
    # if user enters 0 it prints '0' as assumed that the ground/0th term is '0'
    if  nth_number <= 0:
        print(ground_term)
    # if user enters 1 it prints '1' since the code starts its count from 
    # the second term i.e '1,1,2,3...'
    elif nth_number == 1:
        print(first_term)
    # code to print out the nth fibonacci number starting from the second term
    else:
        # sets ground_term and first_term to var1 and var2 respectively
        # just for readability and aesthetics
        var1 = ground_term
        var2 = first_term
        # while loop to carry out the process (nth-number - 2) times
        # the limit of the while loop is set to (nth_number - 2) 
        # because the code skips the ground term and the first term
        while start <= (nth_number - 2):         
            ''' syntax: result calculates the values of the numbers in the sequence
                the value of var1 is changed to var2, which is the former fibonacci 
                number, for the next iteration then the value of var2 is changed to 
                result, which becomes the latter value, for the next iteration then 
                the loop increaments to the next iteration.'''
            ''' example: var1 = 2, var2 = 3 then result = 5. 
                Then var1 = 3 and var2 = 5 then result = 8, etc'''
            result = var1 + var2                 
            var1 = var2
            var2 = result
            start += 1
      
        # outputs the nth fibonacci number
        print(result)            

# ask user to input the fibonacci number to be printed
nth_term = int(input("Enter the fibonacci number to print: "))

# calls function fibonacci          
fibonacci(nth_term)