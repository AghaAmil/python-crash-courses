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

"""
Lesson 3 - finally, else
"""

try:
    print(1 / 0)
except ZeroDivisionError:
    print('Division by Zero Error')
finally:
    print('This code will run no matter what')

# else

try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)

try:
    print(1 / 0)
except ZeroDivisionError:
    print(4)
else:
    print(5)

"""

You are making a digital menu to order food.
The menu is stored as a list of items.
Your program needs to take the index of the item as input and output the item name.

In case the index is not valid, you should output "Item not found".
In case the index is valid and the item name is output successfully, you should output "Thanks for your order".

Sample Input
2

Sample Output
Cheeseburger
Thanks for your order
"""

menu = ['Fries', 'Sandwich', 'Cheeseburger', 'Coffee', 'Soda']

try:
    index = int(input())
    print(menu[index])
except:
    print('Item not found')
else:
    print('Thanks for your order')
