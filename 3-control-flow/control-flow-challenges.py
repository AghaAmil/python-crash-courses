"""
FizzBuzz: Write a Python program that prints the numbers from 1 to 100. But for multiples of three print “Fizz”
instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and
five print “FizzBuzz”.
"""
print('Challenge One \n')  # \n is used to print a black line after this text

for i in range(1, 101):  # range(1, 101) means that start iteration from 1 to 100
    if i % 3 == 0 and i % 5 == 0:
        print('Fizz')
    elif i % 3 == 0:
        print('Buzz')
    elif i % 5 == 0:
        print('FizzBuzz')
    else:
        print(i)
print('End of the Program :) \n')

"""
Factorial Calculator: Write a Python program that takes a number from the user and calculates its factorial. The 
factorial of a number is the product of all positive integers less than or equal to that number.
"""
print('Challenge Two \n')

n = int(input('Enter a number to calculate its factorial: '))
result = 1

while n > 0:
    result *= n  # result = result * n
    n -= 1  # n = n-1
print('Calculation Result is: ')
print(result)
print('\n')

"""
Prime Number Checker: Write a Python program that takes a number from the user and checks whether it’s a prime 
number or not. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and 
itself.
"""
