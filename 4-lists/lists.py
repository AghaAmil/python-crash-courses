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

"""
Lesson 2 - Lists Operations
"""

print('\nGiven a list of numbers, output "bingo" if it contains the input number.')
x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]

entered_num = int(input("Enter a number: "))
if entered_num in x:
    print('Bingo!')
else:
    print('It was not Bingo! :))')

print('\nThe item at a certain index in a list can be reassigned.')
num1 = [3, 53, 92, 47]
print(num1)
num1[2] = 84
print('Some changes')
print(num1)

print('\nLists can also be added the same way strings can be.')
num2 = [1, 2, 3, 4]
print(num2)
num3 = [5, 6, 7, 8]
print(num3)
print('Some magic')
print(num2 + num3)

print('\nAnother magic stuff')
num4 = [5, 39]
num4 += [76, 98]
print(num4[2] // num4[0])

print('\nSimilar to strings, a list can be multiplied by an integer')
num5 = [6, 4, 2, 4]
print(num5)
print('num5 * 3')
num5 *= 3
print(num5)

print('\nTo check if an item is in a particular list, we can use the in operator.')
user_info2 = ['Amir', 'Akbari', 38, 'ID_007868', [6, 9, 1993], 'QA Engineer']
print(user_info2)
print('amir' in user_info2)
print('Amir' in user_info2)
print('38' in user_info2)
print('id_007868' in user_info2)
print(1993 in user_info2)  # That's interesting
print('QA Engineer' in user_info2)

print('\nAnother cool Stuff')
num6 = [10, 9, 8, 7, 6, 5]
num6[0] = num6[1] - 5
if 4 in num6:
    print(num6[3])
else:
    print(num6[4])

print('\nIf you use Persian swear words, this can tell (Free Version)')
answer = input('Write sth, try to be nice: ')
if 'kir' in answer or 'kos' in answer or 'koon' in answer or 'kon' in answer:
    print('Astaghfirullah, Dont say bad words, Koooni.')
else:
    print('Such a good boy!')

print('\nAlso we have this as well: ')
num7 = [1, 2, 3]
print(not 4 in num7)
print(4 not in num7)
print(not 3 in num7)
print(3 not in num7)
