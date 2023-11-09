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
