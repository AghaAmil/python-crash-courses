"""
No one likes homework, but your math teacher has given you an assignment to find the sum of the first N numbers.
Let’s save some time by creating a program to do the calculation for you!
Take a number N as input and output the sum of all numbers from 1 to N (including N).
"""
print('Challenge 1')
print('ake a number N as input and output the sum of all numbers from 1 to N (including N).')
num = int(input('Enter The Preferred  Number: '))

sum = 0
for i in range(1, num + 1):
    sum += i

print(sum)

# This program receives a three-digit input and reverses it. Then, it doubles the reversed number.

print('\nChallenge 2')
input_number = input('Enter a three-digit number: ')
if len(input_number) == 3:
    input_number = int(input_number[::-1])
    print(input_number * 2)
else:
    print('Please enter a valid number')
