"""
Lesson 1 - Debugging
Lesson Takeaways

- Errors in code are known as bugs
- Code is executed line by line from top to bottom
- Code execution is interrupted by bugs
"""

# The practices already mentioned in the sololearn website
# Nothing to add

"""
Lesson 2 - Standards and Best Practices
Lesson Takeaways
 
- You can add comments to your code with the hash symbol #
- Python is a case-sensitive language
- Snake case is the best practice when creating multi-word variable names
"""

# change the previous lesson variables to snake_case variable names


"""
Lesson 3 - Applying Best Practices
Lesson Takeaways

- Spaces are not allowed in variable names
- A variable name cannot start with a number
- Best practices can help you avoid errors
"""

# change the previous lesson variables to snake_case variable names

"""
Lesson 4 - Input and Outputs
Lesson Takeaways
 
- inputs and outputs help machines communicate with the outside world
- the input() instruction allows the user to enter a value into your program
- the print() instruction is used to generate an output
"""

"""
Challenge 1: Display Variables and Strings
Create a Python script that defines two variables, one for your name and another for family name and then display them
"""
print('Enter you name and family name below: ')
first_name = input()
family_name = input()

# the ' ' statement put a str (space) between the first name and family name
full_name = first_name + ' ' + family_name

print(full_name)

"""
Challenge 2: Write a Python script that prompts the user to enter two numbers and then performs the following operations:

Add the two numbers and print the result.
Subtract the second number from the first number and print the result.
Multiply the two numbers and print the result.
Divide the first number by the second number and print the result.
"""

print('Enter two numbers and see the magic')
number1 = input()
number2 = input()

print('Add the two numbers and print the result.')
print(number1 + number2)

print('You got the error right !?')

# Will learn this section later

# print('Subtract the second number from the first number and print the result.')
# print(number2 - number1)
#
# print('Multiply the two numbers and print the result.')
# print(number1 * number2)
#
# print('Divide the first number by the second number and print the result.')
# print(number1 / number2)

"""
Lesson 4 - Data Types
Lesson Takeaways

- computers store and process different data types differently
- string is the data type for text
- integer and float are data types for numbers

"""

# Consider below examplesAli
print('Computer operate with values depends on the date type')
print(3 + 8)
print('Iran ' + 'Man')

