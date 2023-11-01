# Script name: days.py
# Purpose: converts an inputed number of days to years, weeks and days
# Author: Ogunsanya Louis 236345

# Takes input
days =int(input("Input the number of days: "))

# calculates the weeks and years
years = days / 365
weeks = (days - (int(years) * 365)) / 7
days1 = (days - (int(years) * 365)) -(int(weeks) * 7)

#prints an empty line between the in put and output
print("\n")

# output
print("Test Data:")
print("Number of days: ", days)
print("Output:")
print("Years: ", int(years))
print("Weeks: ", int(weeks))
print("Days: ", int(days1))
