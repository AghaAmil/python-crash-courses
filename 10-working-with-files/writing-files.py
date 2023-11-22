"""
Lesson 3 - Writing Files
"""
# this will create a new file called "newfile.txt" and write the content to it.
file = open('file.txt', 'w')

file.write('This sentence has been written by Python... :)')

file.close()

# write in an existing file
file1 = open('file.txt', 'a')

file1.write('\nThis is another text added to existing file.')

file1.close()

# The code below will write to the file and print the number of bytes written.
msg = '\nThis is a sample message!'

file2 = open('file.txt', 'a')

amount_written = file2.write(msg)
print(amount_written)

file2.close()

"""
Take a number N as input and write the numbers 1 to N to the file "numbers.txt", each number on a separate line.

Sample Input
4

Sample Output
1
2
3
4
"""

num = int(input('Enter a Number: '))

file = open("numbers.txt", "w+")

for i in range(1, num + 1):
    content = str(i) + '\n'
    file.write(content)

f = open("numbers.txt", "r")
print(f.read())
f.close()
