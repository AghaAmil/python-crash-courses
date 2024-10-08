"""
In programming, the break and continue statements are used to alter the flow of loops:
break exits the loop entirely
continue skips the current iteration and proceeds to the next one
"""

# Break
for i in range(5):
    if i == 3:
        break
    print(i)

# blank line
print()

# Continue
for i in range(5):
    if i == 3:
        continue
    print(i)

# blank line
print()

"""
Write a function to calculate the sum of elements in a list that are greater than a given number.

Return the sum of the numbers greater than the given number.
If numbers is [1, 2, 3, 4, 5] and n is 3, the return value should be 9 because 4 + 5 is 9.
"""

# create a list of sequence numbers till the entered number
list_num = int(input("create a list of sequence numbers till the entered number: "))

list_of_nums = []

for number in range(1, list_num + 1):
    list_of_nums.append(number)

print(list_of_nums)

n = int(input("Enter the number: "))

print('Return the sum of the numbers greater than the', n)

total = 0

for num in list_of_nums:
    if num < n:
        continue
    else:
        total += num

print('Sum:', total)
