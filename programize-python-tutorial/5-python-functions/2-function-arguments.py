# Function Argument with Default Values
def addition(a=10, b=20):
    return a + b


print('Passing 5 and 4 to the function: ', addition(5, 4))
print('Passing only one number as 2: ', addition(2))
print('Using default values of the function: ', addition())

# blank line
print()


# Python Keyword Argument
def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)


display_info(last_name='Cartman', first_name='Eric')

# blank line
print()

"""
Sometimes, we do not know in advance the number of arguments that will be passed into a function.
To handle this kind of situation, we can use arbitrary arguments in Python.
Arbitrary arguments allow us to pass a varying number of values during a function call.
We use an asterisk (*) before the parameter name to denote this kind of argument.
"""


def find_sum(*numbers):
    result = 0

    for num in numbers:
        result += num

    return result


print(find_sum(2, 34, 45, 5, 2, 6, 9))
print(find_sum(1))
print(find_sum(2, 3))
