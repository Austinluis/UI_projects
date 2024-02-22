# Script name: my_functions.py
# Description: contains simulations of python in-built functions and
# other useful python functions
# Purpose: For reuse in my python code and also because Dr. Ayinla doesn't
# let us use python in-built functions
# Author: Ogunsanya Louis Similoluwa, 236345

# function to get the largest number from a list
# list: list to print the largest number
# return: largest number
def largest(list):
    result = list[0]
    for i in list:
      if i > result:
        result = i
    return(result) 

# function to get the smallest number from list
# list: list to print the smallest number
# return: smallest number
def smallest(list):
    result = list[0]
    for i in list:
      if i < result:
        result = i
    return(result)

# function to get a list from the user
# return: a list
'''while loop with boolean statement 'True' has been used to ask the user
   for input continously untill the break statement is applied. This is 
   most useful in cases where there is a large list and it may be difficult to
   count the numbers on the list.'''
def get_list():
  listed_num = []
  while True:
    num = input("Enter number or '.' to cancel: ") 
    if num == '.': #break statement
      break
    else:
      listed_num += [int(num)] #appends each input to the list
  return(listed_num)

# function to sort a list
# list: list to sort
# reverse: this decides if the list is sorted in ascending or descending order
# default is False which means to print in ascending order
# return: sorted list
def sort(list, reverse = False):
  if reverse == False: #prints in ascending order
    for _ in list:
      for i in range(lenght(list) - 1):
        if list[i] > list[i + 1]:
          b = list[i + 1]
          list[i + 1] = list[i]
          list[i] = b
  elif reverse == True: #prints in descending order
    for _ in list:
      for i in range(lenght(list) - 1):
        if list[i] < list[i + 1]:
          b = list[i + 1]
          list[i + 1] = list[i]
          list[i] = b
  return(list)

# function to find index
# input: list or string
# index_item: the item to return its index
# return: index of item
def index(input, index_item):
  for i in range(lenght(input)):
    if list[i] == index_item:
      index = i
      break
  return(index)

# function to sort a list using binary insertion
# array: list to be sorted
# insert: optional list to append to array
# return: sorted array
def binsort(array, insert = ''): #insert must be a list i.e "[]"
  if insert != '':
    array = array + insert #appends number to the list if insert is specified
  # function to find the right position of key
  # array: list
  # end: postion of key
  # key: item to find right position
  # return: right position
  '''This fuction works by finding the number in the list that
     is just greater than 'key' using binary search
     and returns the index of the number'''
  def binsearch(array, end, key):
    start = 0
    flag = True
    while flag:
      mid = (start + end)//2
      if start == end:
        flag = False
        return(start)
      elif array[mid] <= key:
        start = mid + 1
      else:
        end = mid
       
  for i in range(1,len(array)): #assumes the first element is sorted
    key = array[i]
    position = binsearch(array, i, key)
    while(i > position): #shifts elements to the right of i one step forward
      array[i] = array[i - 1]
      i = i - 1
    array[position] = key #inserts key in the right position
  return(array)

# function to convert a string to a list
# a simulation of the python in-buit split function
# string: string to convert
# delimiter: a delimiter to split the string, default is space
# max_split: maximum  number of splits, default is -1 which is all
# return: splited list
def split(string, delimiter = ' ', max_split = -1):
    # if delimiter is not in the string
    if delimiter != ' ' and delimiter not in string:
        return("Delimiter not found")

    split_strings = []
    current_string = ''
    splits = 0

    for i in string:
        if splits != max_split:
            if i != delimiter:
                current_string += i
            else:
                split_strings = split_strings + [current_string]
                current_string = ''
                splits += 1
        else:
            current_string += i
    split_strings = split_strings + [current_string]
    return(split_strings)

# function to print out the lenght of an input
# simulates the python in-built len function
# input: input to print the lenght
# return: lenght of input
def lenght(input):
    input_lenght = 0
    for i in input:
        input_lenght += 1
    return(input_lenght)

# function to remove leeading and trailling characters from a string
# simulates the string function
# string: string to strip
# character: characters to be removed, default is '\n\t\r\f\v '
# default whitespace characters
# return: striped string
def strip(string, character = '\n\t\r\f\v '):
    start = end = 0
    for i in range(lenght(string)):
        if string[i] not in character:
            start = i
            break
    
    for i in range((lenght(string) - 1), 0, -1): #loops in reverse
        if string[i] not in character:
            end = i
            break

    striped_string = string[start : end + 1]
    return(striped_string)

# function to remove duplicate characters from input
# input: input, could be string or a list
# return: list without duplicate
def strip_dup(input):
    pivot = ''
    striped_string = ''
    striped_list = []
    for i in input:
        if str(i) not in pivot:
            pivot += str(i)
            if type(input) is str: #if input is a string
                striped_string += i
                striped = striped_string
            elif type(input) is list: #if input is a list
                striped_list += [i]
                striped = striped_list
    return(striped)