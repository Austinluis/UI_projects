# Script name: quadratic.py
# Purpose: solves a quadratic equation
# Author: Ogunsanya Louis 236345

import math

# Takes input
print("The syntax of a quadratic equation is ax^2 + bx + c = 0")
a = int(input("Input the value of a and press enter: "))
b = int(input("Input the value of b and press enter: "))
c = int(input("Input the value of c and press enter: "))

# solves for x
# d: discriminant
if a != 0:
    d = math.sqrt((b *b) -(4 * a * c))
    x1 = ((b * -1) + d) / (2 * a)
    x2 = ((b * -1) - d) / (2 * a)
    # outputs the result
    print("The value of x is ", x1, "or", x2)
else:
    # if a = i
    print("Syntax error")
