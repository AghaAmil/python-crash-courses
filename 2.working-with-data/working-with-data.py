"""
Lesson 1 - Data Type Checking
Lesson Takeaways

- the type() instruction is used to check the data type
- the division of two integers always produces a float
"""

# 'strings' cannot do math operations
num1 = 10
num2 = "3"

# This statement will cause an error
# print(num1 + num2)

var_int = 10
var_float = 1.487
var_str = 'amir'

print('var_int = 10')
print(type(var_int))
print('var_float = 1.487')
print(type(var_float))
print('var_str = "amir"')
print(type(var_float))

# Let's check something interesting :)
print(10 / 2)
print(type(10 / 2))

"""
Lesson 2 - Data Conversion
Lesson Takeaways

- you can change the data type of a value with int(), float() and str()
- there are implicit and explicit data type conversions in Python
- str(), int(), float() instructions are explicit conversions
"""

# The issue existed in previous chapter "going deeper with python" is fixed in this lesson.
print('Enter two number to see some math operations')
number1 = float(input())
number2 = float(input())

print('Add the two numbers and print the result.')
print(number1 + number2)

print('Subtract the second number from the first number and print the result.')
print(number2 - number1)

print('Multiply the two numbers and print the result.')
print(number1 * number2)

print('Divide the first number by the second number and print the result.')
print(number1 / number2)

# Let's make some conversions
var1 = '483'
print(type(var1))
print(type(int(var1)))

# Examples of automatic data type conversion
x = 5           # integer
y = 2           # integer
z = x/y         # float (implicit conversion)
print(z)

a = 3           # integer
b = 1.5         # float
c = a + b       # float
print(c)

"""
Lesson 3 - Fixing Data Types
Lesson Takeaways

- you can use explicit data type conversions to avoid bugs in your programs
- int() ensures that the user input is treated as an integer number
- str() can help you concatenate numbers with text
"""

distance = 14
metric = "km"

print('The distance is :')
print(str(distance) + metric)

"""
Lesson 4 - Comparison Operations
Lesson Takeaways

- the Boolean data type has one of two possible values: True or False
- a comparison operation always results in a Boolean
"""

print('19 < 38.4')
print(19 < 38.4)

print('-934 > 2')
print(-934 > 2)

print(type(13 > 34))
print(type(39 < 321))
print(type(True))
print(type(False))

"""
Lesson 5 - Logical Operators
Lesson Takeaways

- logical operations take multiple Boolean values as input
- logical operations produce a single Boolean value as output
- "and" and "or" are examples of logical operations
"""

condition1 = False
condition2 = True

# and operator
print('The "And" Operator')
print('The "and" operation results in a True value only when all the inputs are True at the same time.')

print(condition1 and condition1)
print(condition1 and condition2)
print(condition2 and condition1)
print(condition2 and condition2)

# or operator
print('The "Or" Operator')
print('The "or" logical operation results in a True value if at least one of the inputs is True.')
print(condition1 or condition1)
print(condition1 or condition2)
print(condition2 or condition1)
print(condition2 or condition2)

