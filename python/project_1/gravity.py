# Script name: gravity.py
# Purpose: computes the position of a falling object
# Author: Ogunsanya Louis 236345

# Assigns the values to the variables
# a: acceleration(meters per second square)
# t: time(in seconds)
# v1: initial velocity
# x1: initial position
a = (9.81 * -1)
t = 10
v1 = 0.0
x1 = 0.0

# calculates the positon
# x2: current position
x2 = (0.5 * (a * (t * t)) + (v1 * t) + x1)

# outputs the position
print("Position: ", x2)
