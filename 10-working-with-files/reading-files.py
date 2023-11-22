"""
Lesson 2 - Reading Files
"""

my_file = open('filename.txt')

file_content = my_file.read()
print(file_content)

my_file.close()

print('')

# read byte by byte
file = open('filename.txt')

print(file.read(5))
print(file.read(7))
print(file.read())

file.close()

print('')

# advanced stuff :)))
file1 = open('filename.txt', 'r')

for i in range(21):
    print(file1.read(4))

file1.close()

print('')

# print line by line
file2 = open('filename.txt')

for line in file2.readlines():
    print(line)

file2.close()

print('')

# If you do not need the list for each line, you can simply iterate over the file variable:
file3 = open('filename.txt')

for line in file3:
    print(line)

file3.close()

"""In the output, the lines are separated by blank lines, as the print function automatically adds a new line at the 
end of its output."""

