"""
Lesson one - Lists
"""

print('Write a program that takes an input string and outputs the 3rd character of the string.')
word = input('Enter a string: ')
print(word[2])  # create a blank line

# creating a simple list and print the inside indexes
user_info = ['Amirhossein', 'Moravveji', 28, 'ID_007868', [6, 9, 1993]]
print(user_info)

print('\nPrint out the list items one by one. This list has 5 items inside it.')

for item in range(5):  # Don't know why range should be 5, the code should work when range is 4
    print(user_info[item])

print('\nPython can use nested lists to represent 2D grids, such as matrices.')

samp_matx = [
    [2, 4, 8],
    [6, 2, 9]
]

print('Print out the list items of the create matrix one by one')
print(samp_matx[0][0])
print(samp_matx[0][1])
print(samp_matx[0][2])
print(samp_matx[1][0])
print(samp_matx[1][1])
print(samp_matx[1][2])
