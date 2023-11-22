"""
Lesson 1 - Opening Files
"""

"""
The argument of the open function is the path to the file. If the file is in the current working directory of the 
program, you can specify only its name.
"""

my_file = open('filename.txt')

"""
You can specify the mode used to open a file by applying a second argument to the open function.

Sending "r" means open in read mode, which is the default. 
Sending "w" means write mode, for rewriting the contents of a file.
Sending "a" means append mode, for adding new content to the end of the file.
Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).
"""

# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")


file = open("filename.txt", "w")
# do stuff to the file
file.close()