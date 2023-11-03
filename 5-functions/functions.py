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

input_str = input('Enter any strings and python will tell how many characters are used in your str: ')
print(len(input_str))

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
