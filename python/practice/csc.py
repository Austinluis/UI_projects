# Script name: csc.py
# Purpose: Program to mathematical calculations
# Author: Ogunsanya Louis 236345

import math

# defining functions
# moment of inertia function
def moment_of_inertia():
    if (M == 0 and P != 0):
        inertia = (P * (l**3)) / 3
        linear_density = M * l
    elif (M != 0 and P == 0):
        inertia = (M * (l**2)) / 3
    
    radius_of_gyration = (l / (3**(1/3)))

def main():
    print("Welcome!")
    print("MAT 141")
    print("MAT 121")

    choice = input("Enter an option: ")

    if choice == 1:
        