"""
Lesson 1 - Functions
"""
# Some Built-in python functions
print("Hello world!")

sample_list = list(range(2, 20))
print(sample_list)

print(str(12))

sample_list2 = list(range(10, 20, 3))
print(sample_list2)

"""
Lesson 2 - List Function
"""

# len()
print('\nLen() Function')

print('The length of the above long list is: ')
print(len(sample_list))

sample_list += [20, 21, 22]

print('Some extra numbers is added and the now the length is: ')
print(len(sample_list))

# input_str = input('Enter any strings and python will tell how many characters are used in your str: ')
# print(len(input_str))

# append()
print('\nAppend() Function')

print(sample_list2)

sample_list2.append(6)
print(sample_list2)

sample_list2.append([1, 2, 3])
print(sample_list2)

# insert()
print('\nInsert() Function')

word = ["python", 'easy']
print(word)

word.insert(1, 'is')
word.insert(3, 'and')
word.insert(4, 'fun')
print(word)

# index()
print('\nIndex() Function')

letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters)
print(letters.index('q'))
print(letters.index('s'))
print(letters.index('u'))

# max() - min()
print('\nMax() & Min() Functions')

nums = [3, 43, 98, 7, 86, 323, 9, 13, 297, 872, 70, 72, 46]
print(nums)
print(max(nums))
print(min(nums))

print('min + max')
print(min(nums) + max(nums))

# count(), remove(), reverse()
print('\n Count(), Remove(), Reverse() Functions')
nums2 = [2, 4, 6, 2, 7, 2, 9, 3, 4, 8, 8, 10, 4, 5, 7, 1]
print(nums2)

print('count()')
print(nums2.count(4))
print(nums2.count(2))

print('remove()')
print(nums2.remove(3))
print(nums2)
print(nums2.remove(10))
print(nums2)

print('reverse()')
x = [2, 4, 6, 2, 7, 2, 9]
print(x)
x.reverse()
print(x)

"""
Lesson 3 - Strings Functions
"""

# format()
print('\nFormat() Function')

random_num = [5, 6, 7, 8]
str1 = "Numbers: {0}-{1}-{2}-{3}".format(random_num[0], random_num[1], random_num[2], random_num[3], )
print(str1)

# another example:
print("{0}{1}{0}--{2}".format('abc', 23, 'def'))

# You can also name the placeholders, instead of the index numbers.
print("{x}, {y}, {z}".format(x=5, y='foooz', z=10))

# join()
print('\nJoin() Function')

# join all words in the list with "--" in form of a string
random_list = ['Amir', 'Ali', 'Masoud', 'Mammal']
print(random_list)
print("--".join(random_list))

# join all the all by * and some spaces
random_list1 = ['Apple', 'Orange', 'Cucumber', 'Strawberry']
print(random_list1)
print(" * ".join(random_list1))

# split()
print('\nSplit() Function')

# separate words in string by space
random_str = 'Hello, my name is Amirhossein. and I\'m 30 years old :)'
print(random_str)
print(random_str.split(' '))

# replace()
print('\nReplace() Function')
random_str1 = 'Hello Michael'
print(random_str1)
print(random_str1.replace('Michael', 'World!'))

# upper() & lower()
print('\nUpper() & Lower() Functions')

some_text = 'I love encyclopedia very much'
print(some_text)
print(some_text.upper())

some_text1 = 'I LOVE ULTRA BIG BOOBS VERY MUCH :)) lol'
print(some_text1)
print(some_text1.lower())

"""
Lesson 4 - Making Your Own Functions
"""
print('\nMaking Your Own Function')


def first_function():
    print('Welcome to Python Functions World!')


first_function()


def greeting():
    user = input("Enter Your Name: ")
    print('Hello,', user, "chaghal! :))")


greeting()

# More complex examples will be provided later
