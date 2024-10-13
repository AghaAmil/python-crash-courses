"""
Errors that occur at runtime (after passing the syntax test) are called exceptions or logical errors.
For instance, they occur when we

try to open a file(for reading) that does not exist (FileNotFoundError)
try to divide a number by zero (ZeroDivisionError)
try to import a module that does not exist (ImportError) and so on.
Whenever these types of runtime errors occur, Python creates an exception object.

If not handled properly, it prints a traceback to that error along with some details about why that error occurred.
"""

# print(10 / 0)

print(dir(locals()['__builtins__']))

"""
Errors represent conditions such as compilation error, syntax error, error in the logical part of the code, 
library incompatibility, infinite recursion, etc.

Errors are usually beyond the control of the programmer and we should not try to handle errors.
Exceptions can be caught and handled by the program.

Now we know about exceptions, we will learn about handling exceptions in the next tutorial.
"""
