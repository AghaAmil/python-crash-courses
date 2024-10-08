"""
Challenge 1: Grade Calculator
Create a program that calculates grades for students using nested if-elif statements and a for loop. The program should:

Ask the user for the number of students
For each student, ask for their name and score
Use nested if-elif statements to determine the grade based on the score (A=90-100, B=80-89, C=70-79, D=60-69, F below 60)
Print out each student's name and grade
"""

num_of_students = int(input('Enter the number of the students: '))

for i in range(num_of_students):
    student_name = input('Enter student name: ')
    score = int(input('Enter student score: '))


    if 90 <= score <= 100:
        print('{} with the score of {}, is the A student'.format(student_name, score))
    elif 80 <= score < 90:
        print('{} with the score of {}, is the B student'.format(student_name, score))
    elif 70 <= score < 80:
        print('{} with the score of {}, is the C student'.format(student_name, score))
    elif 60 <= score < 70:
        print('{} with the score of {}, is the D student'.format(student_name, score))
    elif 0 <= score < 60:
        print('{} with the score of {}, is the F student'.format(student_name, score))
    else:
        print('Enter a valid score')

    # blank line
    print()

