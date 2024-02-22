# Script name: score.py
# Purpose: accepts scores of 5 courses and finds the average score
# Author: Ogunsanya Louis Similoluwa 236345

# main code in for loop
# asks user for score 5 times
c_score = []
total_score = 0
for _ in range(5):
    # asks for scores
    course_score = float(input("Enter the score: "))
    # appends the scores to a list
    c_score.append(course_score)

# adds the scores    
for i in c_score:
    total_score += i    
# calculates the average score
avg_course_score = total_score / 5
# prints the average score
print("Your average score is: ", avg_course_score)