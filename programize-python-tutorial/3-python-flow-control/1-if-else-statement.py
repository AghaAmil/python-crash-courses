# Python if...else Statement

student_score = int(input("Enter Your Exam Score: "))

if student_score >= 90:
    print('You are a grade A Student')
elif student_score >= 75:
    print('You are a grade B Student')
elif student_score >= 65:
    print('You are a grade C Student')
elif student_score >= 40:
    print('You are a grade D Student')
elif 0 <= student_score < 40:
    print('You are a failed Student')
else:
    print('Enter a Valid Score')

# blank line
print()

# Python Nested if Statements
input_number = int(input("Enter a positive or negative number: "))

if input_number >= 0:
    if input_number == 0:
        print('The Number is Zero')
    else:
        print('The Number is Positive')
else:
    print('The Number is Negative')

