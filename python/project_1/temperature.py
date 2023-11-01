# Script name: temperature.py
# Purpose: Coverts the integer stored in the variable 'fahrenheit' in Fahrenheit to Celsius
# The data type of the output must be a float
# Assuming the variable fahrenheit is fixed
# Author: Ogunsanya Louis 236345

# I assign a value to the variable fahrenheit since it is assumed the the variable id fixed
fahrenheit = 50

# converts the variable fahrenheit to celsius
Celsius = float(((fahrenheit - 32) * 5) / 9)

# outputs the converted result
print("Temperature in degree Fahrenheit: ", fahrenheit)
print("Temperature in degree Celsius: ", Celsius)
