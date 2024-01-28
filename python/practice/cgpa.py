# Script name: cgpa.py
# Purpose: outputs the result of a student and calculates their cgpa
# Author: Ogunsanya Louis Similoluwa 236345

# imports time module to cause intentional delays for better user experience and dramatic effect
import time

# collects students data and the number of courses offered
name = input("Enter your Firstname: ")
while True:
    if name.isalpha():
        print("...")
        time.sleep(1)
        break
    name = input("Enter a valid Firstname: ")
matric = input("Enter your Matric number: ")
matric_status = True
while matric_status:
    if matric.isdigit():
        if len(matric) == 6:
            print("...")
            time.sleep(1)
            matric_status = False
        else:
            matric = input("Your matric is a 6 digit number: ")
            matric_status = True
    else:
        matric = input("Enter a valid matric number: ")
        matric_status = True
courses_offered = input("Enter the number of courses offered: ")
while True:
    if courses_offered.isdigit():
        print("Loading...")
        time.sleep(1)
        break
    courses_offered = input("Enter a valid number: ")

# prints a new line and the a line of asterisks after collecting students data
print('\n')
print("*" * 30)

# sets the number of times the user is asked for details on the courses offered
repeat = range(int(courses_offered))

# defining variables and declaring strings
total_courses_passed = 0
total_courses_failed = 0
total_units = 0
wgpa = 0
c_name = []
c_unit = []
c_score = []
ga = []
c_grade = []

# main code in for loop
# sets number of times student is asked for details on courses offered
for _ in repeat:
    # asks for details on courses offered
    course_name = input("Enter the course code: ")
    course_unit = int(input("Enter the course unit: "))
    course_score = float(input("Enter your score: "))
    # appends the inputs
    c_name.append(course_name)
    c_unit.append(course_unit)
    c_score.append(course_score)
    # prints a line of asterisks after asking for input on courses offered
    print("*" * 30)
    # calculates grade point average and assigns grades
    if course_score >= 70:
        gpa = course_unit * 4
        course_grade = 'A'
    elif course_score >= 60 and course_score < 70:
        gpa = course_unit * 3
        course_grade = 'B'
    elif course_score >= 50 and course_score < 60:
        gpa = course_unit * 2
        course_grade = 'C'
    elif course_score >= 45 and course_score < 50:
        gpa = course_unit * 1
        course_grade = 'D'
    elif course_score < 45:
        gpa = course_unit * 0
        course_grade = 'E'
    # appends input
    ga.append(gpa)
    c_grade.append(course_grade)
    # calculate total number of courses passed or failed by student
    if course_score >= 45:
        total_courses_passed += 1
    else:
        total_courses_failed += 1
    # calculates total number of units offered by student
    total_units += course_unit
    # calculates weighted grade point average
    wgpa += gpa
    # calculates culmulative grade point average
    cgpa = wgpa / total_units

# output
# prints result
print('\n')
print("*" * 50)
print("NAME: ", name)
print("MATRIC NO: ", matric)
print("*" * 50)
print("*" * 50)
print("COURSE CODE\tUNIT\tSCORE\tGPA\tGRADE")
for course_name, course_unit, course_score, gpa, course_grade in zip(c_name, c_unit, c_score, ga, c_grade):
    print(f"{course_name}\t\t{course_unit}\t{course_score}\t{gpa}\t  {course_grade}")
print("*" * 50)
print("Total number of courses passed: ", total_courses_passed)
print("Total number of courses failed: ", total_courses_failed)
print("Total units registered for: ", total_units)
print("Weighted grade point average: ", wgpa)
print("Culmulative grade point average: ", round(cgpa, 1))
if cgpa >= 3.5:
    print("Class of Degree: First Class")
elif cgpa >= 3.0 and cgpa < 3.5:
    print("Class of Degree: Second class upper")
elif cgpa >= 2.0 and cgpa < 3.0:
    print("Class of Degree: Second class lower")
elif cgpa >= 1.0 and cgpa < 2.0:
    print("Class of Degree: Third class")
elif cgpa < 1.0:
    print("Fail! Advised to withdraw")
print("*" * 50)
print("*" * 50)
