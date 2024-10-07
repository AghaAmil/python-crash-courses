"""
Write a function that calculates the new price of an item after the discount using lambda function

Sample Input
50
10

Sample Output
45.0
"""
price = int(input('Enter the price of the item: '))
discount_percentage = int(input('Enter the discount percentage: '))

new_price = (lambda a, b: a - (a * b / 100))(price, discount_percentage)

print('The item price after the discount is: ', new_price)

"""
You work on a payroll program.
Given a list of salaries, you need to take the bonus (in percent) everybody is getting as input
and increase all the salaries by that amount. Output the resulting list.
"""

salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input('Enter the bonus percentage: '))

salary_cal = list(map(lambda x: int(x + (x * bonus / 100)), salaries))

print(salary_cal)

"""
Finding prime numbers is a common coding interview task.
The given code defines a function isPrime(x), which returns True if x is prime.
You need to create a generator function primeGenerator(), that will take two numbers as arguments, and use the
isPrime() function to output the prime numbers in the given range (between the two arguments).

Sample Input
10
20

Sample Output
[11, 13, 17, 19]
"""


# prime number: [1, 2, 3, 5, 7, 11 ...]


def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for num in range(2, x):
        if x % num == 0:
            return False
    return True


def primeGenerator(num1, num2):
    for i in range(num1, num2):
        if isPrime(i):
            yield i


print('\nWrite a code to output the prime numbers in the given range (between the two arguments). ')
input1 = int(input('Enter the first number: '))
input2 = int(input('Enter the second number: '))

print(list(primeGenerator(input1, input2)))

"""
You are working on an invoicing system.
The system has an already defined invoice() function, which takes the invoice number as argument and outputs it.
You need to add a decorator for the invoice() function, that will print the invoice in the following format:

Sample Input
42

Sample Output
*********
INVOICE #42
*********
END OF PAGE
"""


def decor(func):
    def invoice_temp(num):
        print('*********')
        func(num)
        print('*********')
        print("END OF PAGE")

    return invoice_temp


@decor
def invoice(num):
    print('INVOICE #', num)


invoice(input('\nEnter Your invoice Number: '))

"""
The given code defines a recursive function convert(), which needs to convert its argument from decimal to binary.
However, the code has an error.
Fix the code by adding the base case for the recursion, then take a number from user input and call the convert()
function, to output the result.

Sample Input
8

Sample Output
1000
"""


# Corrected function
def convert(num):
    if num == 0:
        return 0
    else:
        return num % 2 + 10 * convert(num // 2)


int_number = int(input('\nEnter an integer to convert it to binary number: '))
print('The converted number to binary is: ', convert(int_number))

"""
Calculation for num = 3

convert(3)   -->     3 % 2 + 10 * convert(3 // 2) --> 1 + 10 * convert(1) --> 1 + 10 x 1 = 11
convert(1)   -->     1 % 2 + 10 * convert(1 // 2) --> 1 + 10 * convert(0) --> 1 + 0
"""

"""
The given code defined a function called my_min(), which takes two arguments and returns the smaller one.
You need to improve the function, so that it can take any number of variables, so that the function call works.
"""


# Improved function
def my_min(*args):
    r = args[0]
    for num in args:
        if num < r:
            r = num
    return r


print(my_min(8, 13, 4, 42, 120, 7, 1))
