# Script name: waec.py
# Purpose: uses a switch to print out the waec grade
# Author: Ogunsanya Louis Similoluwa 236345

# defining each case
def grade_A():
    return('A1')
def grade_B2():
    return('B2')
def grade_B3():
    return('B3')
def grade_C4():
    return('C4')
def grade_C5():
    return('C5')
def grade_C6():
    return('C6')
def grade_D7():
    return('D7')
def grade_E8():
    return('E8')
def grade_F9():
    return('F9')

# switch to call case in dictionary
switch = {
    range(75,101):grade_A,
    range(70,75):grade_B2,
    range(65,70):grade_B3,
    range(60,65):grade_C4,
    range(55,59):grade_C5,
    range(50,55):grade_C6,
    range(45,50):grade_D7,
    range(40,45):grade_E8,
    range(0,40):grade_A,
}

# runs code
def grade(score):
    for key, value in switch.items():
        if score in key:
            return value()

# asks for grade
_score_ = int(input("Enter the score: "))
print("Grade: ", grade(_score_))