# Python while Loop

total = 0
counter = 0

input_number = int(input('Enter a number (ENTER ZERO TO STOP): '))

while input_number != 0:
    input_number = int(input('Enter a number (ENTER ZERO TO STOP): '))
    total += input_number
    counter += 1

print('The Sum Of Entered Numbers: ', total)
print('Total Numbers Added: ', counter)

