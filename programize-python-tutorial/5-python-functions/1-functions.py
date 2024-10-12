def greeting(name, family_name):
    print('Welcome', name, family_name)
    print('Let\'s us learn python!')


greeting('Amirhossein', 'Moravveji')

# blank line
print()


# The return Statement
def addition(a, b):
    return a + b


sum_of_nums = addition(10, 4)
print(f'Sum of 10 and 4: {sum_of_nums}')

# blank line
print()

"""
The pass statement serves as a placeholder for future code, preventing errors from empty code blocks.
"""


def future_function():
    pass


# this will execute without any action or error
future_function()

# Python Library Function
import math

# sqrt computes the square root
square_root = math.sqrt(4)

print("Square Root of 4 is", square_root)

# pow() comptes the power
power = pow(2, 3)

print("2 to the power 3 is", power)
