# Some Challenges
#
print('# Write a Python expression that checks if a number x is both greater than 10 and less than 20.')

ch1_num = float(input('Enter a number x: (Input Type Is Float)'))  # a text displayed when input prompt is executed
print((ch1_num > 10) and (ch1_num < 20))

print('Given three variables a, b, and c, write a Python expression that checks if a is equal to b or c.')
ch2_a = float(input('Enter a value to be stored in variable "a" (Input Type Is Float)'))
ch2_b = float(input('Enter a value to be stored in variable "b" (Input Type Is Float)'))
ch2_c = float(input('Enter a value to be stored in variable "c" (Input Type Is Float)'))

# basic form of comparison is added based on what have been taught in the lesson
print('True is printed if a if a is equal to b or c')
print((ch2_a == ch2_b) or (ch2_a == ch2_c))

# The following challenges will be added later.

"""
Write a Python expression that checks if a string s contains both the letters 'a' and 'b'.

Given two variables x and y, write a Python expression that checks if either x is equal to 5 or y is equal to 10.

Write a Python expression that checks if a list nums contains at least one even number and at least one odd number.

Given three variables p, q, and r, write a Python expression that checks if p is greater than q and q is greater than r.

Write a Python expression that checks if a string s starts with either 'A' or 'B' and ends with 'Z'.

Given two variables x and y, write a Python expression that checks if x is equal to 0 or y is not equal to 0.

Write a Python expression that checks if a list words contains either the word 'hello' or the word 'world', or both.

Given three variables a, b, and c, write a Python expression that checks if a is less than b or b is less than c, 
but a is not less than c.
"""
