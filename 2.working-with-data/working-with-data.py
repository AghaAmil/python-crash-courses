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