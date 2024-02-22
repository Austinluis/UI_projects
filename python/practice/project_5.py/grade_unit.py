# Script name: grade_unit.py
# Purpose: prints out the grade unit of a score
# Author: Ogunsanya Louis Similoluwa 236345

# while loop executes the code continuosly until break statement is applied
while True:
    # asks for score
    score = input("Enter the score or enter 'exit' to cancel: ")
    if score == 'exit': #break statement
        break
    elif float(score) >= 80: #80 and above
        grade = 'Excellent'
        unit = 4
    elif float(score) >= 60 and score < 80: #60 to 79
        grade = "Good"
        unit = 3
    elif float(score) >= 46 and score < 60: #46 to 59
        grade = "Average"
        unit = 2
    elif float(score) >= 41 and score < 46: #41 to 45
        grade = "Pass"
        unit = 1
    elif float(score) <= 40: #less than 40
        grade = "Fail"
        unit = 0
    # prints out the appropriate grade and unit
    print("Grade: ", grade)
    print("Unit : ", unit)