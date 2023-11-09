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
