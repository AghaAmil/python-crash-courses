"""
In programming, type conversion is the process of converting data of one type to another. For example: converting int data to str.
There are two types of type conversion in Python.

Implicit Conversion - automatic type conversion
Explicit Conversion - manual type conversion
"""

# Python Implicit Type Conversion
number_1 = 35
number_2 = 13.84

new_num = number_1 + number_2

print('Value: ', new_num)
print('Data Type: ', type(number_2))

# blank line
print()

# Explicit Type Conversion
my_string = '12'
my_number = 61

print('Type of the string before conversion: ', type(my_string))

# explict conversion
my_string = int(my_string)

print('Type of the string after conversion: ', type(my_string))

new_number = my_number + my_string

print('Value ', new_number)
print('Data Type: ', type(new_number))
