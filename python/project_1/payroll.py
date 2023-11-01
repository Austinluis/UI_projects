# Script name: payroll.py
# Purpose: prompts new staff members for their biodata and outputs thier netpay
# Author: Ogunsanya Louis 236345

# asks for new staff biodata
print("Welcome!")
first_name = input("Input your First name and press enter: ")
last_name = input("Input your Last name and press enter: ")
birth_year = int(input("Input your Year of Birth and press enter: "))
next_kin = input("Input your Next of Kin and press enter: ")
address = input("Input your Residential Adress and press enter: ")

# calculates the net pay
# gross = gross pay of workers
gross = 100000
retirement = birth_year + 65
tax = 0.125 * gross
pension = 0.075 * gross
health = 0.05 * gross
housing = 0.05 * gross
net_pay = gross - tax - pension - health - housing

# prints a line between the input and output
print("\n")

intro_for_gross_pay = "Details about your year of retirement and monthly salary package:"

# prints astericks
print("*" * len(intro_for_gross_pay))

# output
print("Huge Congratulations on joining Kolesolution ", first_name,last_name)
print(intro_for_gross_pay)
print("Year of Retirement is ", retirement)
print("Monthly Gross Pay is  ", gross, "Naira")
print("Monthly Deductions as follows:")
print("Tax Deducion of 12.5%: ", tax)
print("Pension Contribution of 7.5%: ", pension)
print("Health Insurance of 5%:", health)
print("Housing Contribution of 5%: ", housing)
print("Monthly Net Pay is ", net_pay, "Naira")

# prints asterisks
print("*" * len(intro_for_gross_pay))
