# Arithmetic Operators in Python
a = 7
b = 2

print('The Number a = {}. The Number b = {}'.format(a, b))

# addition
print('Sum: ', a + b)
# subtraction
print('Subtraction: ', a - b)
# multiplication
print('Multiplication: ', a * b)
# division
print('Division: ', a / b)
# floor division
print('Floor Division: ', a // b)
# modulo
print('Modulo: ', a % b)
# a to the power b
print('Power: ', a ** b)
# print blank line
print()

# Assignment Operators

# assign 10 to a
a = 10
# assign 5 to b
b = 5
# assign the sum of a and b to a
a += b  # a = a + b
print(a)

# Python Comparison Operators

# print blank line
print()

a = 5
b = 2

print(a > b)  # True

# print blank line
print()

a = 5
b = 2

# equal to operator
print('a == b =', a == b)
# not equal to operator
print('a != b =', a != b)
# greater than operator
print('a > b =', a > b)
# less than operator
print('a < b =', a < b)
# greater than or equal to operator
print('a >= b =', a >= b)
# less than or equal to operator
print('a <= b =', a <= b)

# print blank line
print()

# Python Logical Operators
a = 5
b = 6

print((a > 2) and (b >= 6))  # True

# logical AND
print(True and True)  # True
print(True and False)  # False

# logical OR
print(True or False)  # True

# logical NOT
print(not True)  # False

# print blank line
print()

'''
Python language offers some special types of operators like the identity operator and the membership operator.
They are described below with examples.

In Python, 'is' and 'is not' are used to check if two values are located at the same memory location.
'''

x1 = 5
y1 = 5
x2 = 'hello'
y2 = 'hello'
x3 = [1, 2, 3]
y3 = [1, 2, 3]

print(x1 is not y1)  # prints False
print(x2 is y2)  # prints True
print(x3 is y3)  # prints False
'''
But x3 and y3 are lists. They are equal but not identical.
It is because the interpreter locates them separately in memory, although they are equal.
'''

# print blank line
print()

'''
In Python, in and not in are the membership operators.
They are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).
'''

message = 'Hello world'
dict1 = {1: 'a', 2: 'b'}

# check if 'H' is present in message string
print('H' in message)  # prints True

# check if 'hello' is present in message string
print('hello' not in message)  # prints True

# check if '1' key is present in dict1
print(1 in dict1)  # prints True

# check if 'a' key is present in dict1
print('a' in dict1)  # prints False
