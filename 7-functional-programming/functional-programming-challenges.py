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
