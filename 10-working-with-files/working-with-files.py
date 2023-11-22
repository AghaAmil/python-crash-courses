"""
Lesson 4 - Working with files
"""

# This ensures that the file is always closed, even if an error occurs.
try:
    file = open('file.txt')
    cont = file.read()
    print(cont)
finally:
    file.close()

print('')

"""An alternative way of doing this is by using with statements.This creates a temporary variable (often called f),  
which is only accessible in the indented block of the with statement."""

"""
The file is automatically closed at the end of the with statement, even if exceptions occur within it.
"""
with open('filename.txt') as f:
    print(f.read())

"""
You are given a books.txt file, which includes book titles, each on a separate line.
Create a program to output how many words each title contains, in the following format:

Line 1: 3 words
Line 2: 5 words
...
"""

with open('books.txt') as f:
    line_num = 0
    for line in f.readlines():
        line_num += 1
        print("Line" + " " + str(line_num) + ":" + " " + str(len(line.split())) + " " + "words")
