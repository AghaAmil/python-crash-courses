"""
Lesson one - Lists
"""

print('Write a program that takes an input string and outputs the 3rd character of the string.')
word = input('Enter a string: ')
print(word[2])

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

"""
Lesson 3 - For Loops
"""

print('\nGiven a list of numbers, calculate their sum using a for loop.')
num8 = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]
print(num8)

sum_of_numbers = 0
for numbers in num8:
    sum_of_numbers += numbers

print(sum_of_numbers)

print('\nWhat is the output of this code?')
num9 = [1, 2, 3, 4]
res = 0

for x in num9:
    if x % 2 == 0:
        continue
    else:
        res += x

print(res)

print('\nFill in the blanks to loop over the list and output the numbers which are bigger than 4 and smaller than 25.')
num_list = [1, 5, 9, 10, 2, 11, 24, 90, 100, 17, 25, 645, 42, 50, 22, 14, 40, 23, 24, 87, 66, 54]

for x in num_list:
    if 4 < x < 25:
        print(x)

print('\nThe code below outputs each item in the list and adds an exclamation mark at the end:')
words = ["hello", "world", "spam", "eggs", 'kir', 'koon', 'kos khol', 'antar']

for x in words:
    print(x + '!')

print('\nA for loop can be used to iterate over strings.')
string_1 = "testing for loops and iteration concepts and other stuff"

count = 0
count_double = 0
for x in string_1:
    if x == 't':
        count += 1

print(count)
print(count_double)

# later write a program to check if there repeated letter one after each other in a string
print("\nSomething that i've created myself.")
num10 = [33, 27, 82, 43, 87, 873, 39, 83, 28, 73, 75, 735, 183]
print(num10)

for x in num10:
    print(x)
    if x % 7 == 0:
        print('First number in the list which is dividable by 7')
        break

"""
Lesson 4 - Ranges
"""

print('\nWrite a program that takes two integers as input and outputs the range of numbers between the two inputs as a '
      'list.')
print('The output sequence should start with the first input number and end the last number')

input_number1 = int(input('Enter the first number: '))
input_number2 = int(input('Enter the second number: '))

print(list(range(input_number1, input_number2 + 1)))

print('\nSequence of numbers with step')
print(list(range(5, 26, 2)))

print('\nWant to go backward? No problem! We can also create a list of decreasing numbers, using a negative number '
      'as the third argument.')
print(list(range(20, 0, -2)))  # pay attention to the result

"""
Lesson 4 - List Slices
"""

print('\nWrite a program that takes a string as input and outputs the last character of that string.')
input_string = input('Enter whatever you want:')
print(input_string[-1:])

list_of_squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]
print(list_of_squares)
print('Display list[3:9]')
print(list_of_squares[3:9])
print('Display list[0:5]')
print(list_of_squares[0:5])
print('Display list[1:11:2]')
print(list_of_squares[1:11:2])
print('Display list[:3]')
print(list_of_squares[:3])
print('Display list[6:]')
print(list_of_squares[:6])
print('Display list[7:2:-1]')
print(list_of_squares[7:2:-1])
print('Display list[3:-2]')
print(list_of_squares[3:-2])

print('Enter whatever string you want, i will reverse it :) ')
input_word = input('Enter Your word: ')
print(input_word[::-1])
print('Your Correct word/sentence:')
print(input_word)
