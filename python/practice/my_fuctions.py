# Script name: my_functions.py
# Description: contains simulations of python in-built functions and
# other useful python functions
# Purpose: For reuse in my python code amd also because Dr. Ayinla doesn't
# let us use python in-built functions
# Author: Ogunsanya Louis Similoluwa, 236345

# function to get the largest number
'''this function sets the value of result to be the greater number between each
   number on the list and its current value as it goes through all the items in the list.'''
def largest(list):
    result = list[0] #sets the inital value of result to the first number on the list
    for i in list:
      if i > result:
        result = i
    return(result) #returns the largest number

# function to get the smallest number
'''this function sets the value of result to be the lesser number between each
   number on the list and its current value as it goes through all the items in the list.'''
def smallest(list):
    result = list[0] #sets the inital value of result to the first number on the list
    for i in list:
      if i < result:
        result = i
    return(result) #returns the smallest number

# function to get a list from the user
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
      listed_num.append(int(num)) #appends each input to the list
  return(listed_num)

# function to print a list in ascending order
'''compares between an item on the list and the next item and swaps the items
   if the former is greater''' 
def ascend(list):
  for _ in list: #repeats the code to achieve a completely sorted list
    # swaps the items if condition is met
    for i in range(len(list) - 1):
      if list[i] > list[i + 1]: #compares items
        b = list[i + 1] #assigns the next item to b
        list[i + 1] = list[i] #swaps the next item to the former item
        list[i] = b #swaps the former item to the next item
  return(list) #returns sorted list

# function to print a list in descending order
'''compares between an item on the list and the next item and swaps the items
   if the former is lesser''' 
def descend(list):
  for _ in list: #repeats the code to achieve a completely sorted list
    # swaps the items if condition is met
    for i in range(len(list) - 1):
      if list[i] < list[i + 1]: #compares items
        b = list[i + 1] #assigns the next item to b
        list[i + 1] = list[i] #swaps the next item to the former item
        list[i] = b #swaps the former item to the next item
  return(list) #returns sorted list

# function to sort a list
'''compares between an item on the list and the next item and swaps the items
   if the former is lesser or greater as the case may apply''' 
def sort(list, reverse):
  if reverse == False: #prints in ascending order
    for _ in list: #repeats the code to achieve a completely sorted list
      # swaps the items if condition is met
      for i in range(len(list) - 1):
        if list[i] > list[i + 1]: #compares items
          b = list[i + 1] #assigns the next item to b
          list[i + 1] = list[i] #swaps the next item to the former item
          list[i] = b #swaps the former item to the next item
  elif reverse == True: #prints in descending order
    for _ in list: #repeats the code to achieve a completely sorted list
      # swaps the items if condition is met
      for i in range(len(list) - 1):
        if list[i] < list[i + 1]: #compares items
          b = list[i + 1] #assigns the next item to b
          list[i + 1] = list[i] #swaps the next item to the former item
          list[i] = b #swaps the former item to the next item
  return(list) #returns sorted list

# function to find the index of a number
def index(list, index_num):
  for i in range(len(list)):
    if list[i] == index_num:
      index = i
      break
  return(index)

# function to sort a list using binary insertion
def binsert(array, item):
  def binsearch(array, end, key):
    start = 0
    flag = True
    while flag:
      mid = (start + end)//2
      if start == end:
        return(start)
      elif array[mid] <= key:
        start = mid + 1
        flag = True
      else:
        end = mid
        flag = True

  array = array + [item]
  for i in range(1,len(array)):
    key = array[i]
    position = binsearch(array, i, key)
    while(i > position):
      array[i] = array[i - 1]
      i = i - 1
    array[position] = key
  return(array)