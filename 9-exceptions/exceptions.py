"""
Lesson 1 - Exceptions

An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program.
"""

# ZeroDivisionError
num1 = 19
num2 = 0
# print(num1 / num2)    # ZeroDivisionError: division by zero

"""
Different exceptions are raised for different reasons. 
Common exceptions:

ImportError: an import fails;
IndexError: a list is indexed with an out-of-range number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly; 
TypeError: a function is called on a value of an inappropriate type;
ValueError: a function is called on a value of the correct type, but with an inappropriate value.
"""

# print('7' + 4)        # TypeError is raised

"""
Lesson 2 - Exception Handling
"""
try:
    print(num1 / num2)
    print('Calculation is done')
except ZeroDivisionError:
    print('An error Occurred')
    print('Due to zero division')

print('')
# multiple exception handling

try:
    var = 10
    print(var + 'hello')
    print(var / 2)
except ZeroDivisionError:
    print('Faced a zero division error')
except (TypeError, ValueError):
    print('Type or Value Occurred')

print('')
# no exception defined

try:
    word = 'akbar'
    print(word / 0)
except:
    print('Faced an error')

"""
An ATM machine takes the amount to be withdrawn as input and calls the corresponding withdrawal method.
In case the input is not a number, the machine should output "Please enter a number".
Use exception handling to take a number as input, call the withdraw() method with the input as its argument, 
and output "Please enter a number", in case the input is not a number.
"""


def withdraw(amount):
    print(str(amount) + " withdrawn!")


# your code goes here
try:
    amount = int(input('Enter the amount of withdraw: '))
    withdraw(amount)
except ValueError:
    print('Please enter a number')

