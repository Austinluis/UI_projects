# Script name: bubblesort.py
# Purpose: Sorts a list using bubble sort 
# and inserts a number into the list at the right position using binary search
# Author: Ogunsanya Louis Similoluwa, 236345

# function to sort a list using bubble sort
# list: list to sort
# return: sorted list
def sort(list):
  if reverse == False: #prints in ascending order
    swapped = True
    while swapped: #outer loop to repeat until list is completely sorted
      swapped = False #ends outer loop if no swap was made
      for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
          # swaps the numbers
          b = list[i + 1]
          list[i + 1] = list[i]
          list[i] = b
          swapped = True #runs outer loop if any swaps were made
  elif reverse == True: #prints in descending order
    swapped = True
    while swapped: #outer loop to repeat until list is completely sorted
      swapped = False #ends outer loop if no swap was made
      for i in range(len(list) - 1):
        if list[i] < list[i + 1]:
          # swaps the numbers
          b = list[i + 1]
          list[i + 1] = list[i]
          list[i] = b
          swapped = True #runs outer loop if any swaps were made
  return(list)

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

# function to sort a list using binary insertion
# array: list to be sorted
# insert: optional number to insert into array
# return: sorted array
def binsort(array, insert = ''):
  sorted_list = sort(array)
  if insert != '':
    sorted_list = sorted_list + [insert] #appends number to the list if insert is specified
    key = insert
    i = len(array)
    position = binsearch(sorted_list, i, insert)
    while(i > position): #shifts elements to the right of i one step forward
      sorted_list[i] = sorted_list[i - 1]
      i = i - 1
    sorted_list[position] = key #inserts key in the right position
  return(sorted_list)

list = [3,4,1,7,8]
print(binsort(list, 5))