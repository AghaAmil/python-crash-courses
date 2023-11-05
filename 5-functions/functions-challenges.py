"""
This function takes a long list as an argument and tells the numbers in list are odd or even and categorize them
into a new list
"""
# list_of_nums = [3, 4, 972, 48, 27, 297, 83, 15, 37, 93, 74, 67, 98, 30, 10, 973, 3810, 973, 28, 34, 74, 93, 82, 23, 1]
# print(list_of_nums)
print('This function gets a list of numbers and categories them into odd and even numbers')
nums_list_str = input("Enter preferred list of numbers and separate them by space: ")
nums_list = nums_list_str.split()
print(nums_list)


def divider(input):
    even_nums = []
    odd_nums = []
    for i in range(len(input)):
        num = int(input[i])
        if num % 2 == 0:
            even_nums.append(num)
        else:
            odd_nums.append(num)
    print('This is the list of even numbers: ', even_nums)
    print('This is the list of odd numbers: ', odd_nums)


divider(nums_list)
"""
The given code takes a text and a word as input and passes them to a function called search().
The search() function should return "Word found" if the word is present in the text, or "Word not found", if it’s not.

Sample Input
"This is awesome"
"awesome"

Sample Output
Word found
"""
print('\nYou’re working on a search engine')
text = input('Enter any sentence or words: ')
word = input('Enter a word to start the search in sentence": ')


def search(text, word):
    if word in text:
        return 'Word found in the text'
    else:
        return 'Word not found in the text'


print(search(text, word))
