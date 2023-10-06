"""
Lesson 1 - Memory and Variable
Lesson Takeaway

- Computer programs use variables to remember important information
- A variable has a name and a value
- You can create a variable by connecting the name and the value with an equal sign =
"""

# Let's create some variables
name = 'Amirhossein'
lastName = 'Moravveji'
city = 'Tehran'

"""
Lesson 2 - Text Data
Lesson Takeaway

#  A piece of text is called a string
# Strings require quotation marks
# The print() statement is used to send a value to the screen
"""

# I know this code to display the variables
print(name)
print(lastName)
print(city)

"""
# Lesson 3 - Numerical Numbers
# Lesson Takeaway

# Numerical values can be stored in variables
# You can access the value stored in a variable by calling its name
# Numerical data should not be surrounded by quotation marks
"""

# Add the two numbers and print the result.
print(41 + 17)

# Subtract the second number from the first number and print the result.
print(17 - 41)

# Multiply the two numbers and print the result.
print(74 * 36)

# Divide the first number by the second number and print the result
print(74 / 36)

currentYear = 2023
yearBorn = 1993
print('Your age is :')
print(currentYear - yearBorn)

"""
Challenge 1: Display Variables and Strings
Create a Python script that defines two variables, one for your name and another for your age. Then, use the print()
statement to display a message like "My name is [name] and I am [age] years old.
"""

userName = 'Aroochi'
age = 2
print('My name is: ')
print(userName)
print('and I am very young')
print(age)

"""
# Lesson 4 - Working with Variables
# Lesson Takeaway

- You can run calculations using the values stored in variables
- You can store the result of a calculation in a variable
- Updating the value of a variable is called reassigning a variable
"""

num1 = 10
num1 = 42
print(num1)

num1 = num1 + 4.3
print(num1)

num2 = 83
num3 = 34
print(83 % 34)
