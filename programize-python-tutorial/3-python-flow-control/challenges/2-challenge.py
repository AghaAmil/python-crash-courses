"""
Challenge 2: Prime Number Generator
Write a program that generates prime numbers up to a given limit using a for loop and if-elif statements. The program should:

Ask the user for the upper limit
Use a for loop to iterate from 2 to the limit
For each number, check if it's prime using if-elif statements
Print out all prime numbers found
"""

limit = int(input("Enter the limit up to which you want to generate prime numbers: "))

for num in range(2, limit + 1):
    is_prime = True
    # Check if the current number is divisible by any number from 2 to its square root
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    # If the number is prime, print it
    if is_prime:
        print(num, end=' ')

