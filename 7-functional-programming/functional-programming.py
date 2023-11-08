"""
Lesson 1 - Functional Programming
"""


# higher-order functions
def upper_func(func, arg):
    return func(func(arg))


def lower_func(arg):
    return (arg * 2 + 3) / 2.5


print(upper_func(lower_func, 10))


# pure and impure functions

# pure function
def pure_func(x, y):
    temp = x + 2 * y
    return temp / (x * 2) + y


print(pure_func(5, 6))

# Impure function
z = 12


def impure_func(x, y):
    temp = x + (2 * y) + (z * 3)
    return temp / (x * 2) + y


print(impure_func(5, 6))

"""
Using pure functions has both advantages and disadvantages.
Pure functions are:

- easier to reason about and test.
- easier to run in parallel.
- more efficient. Once the function has been evaluated for an input, the result can be stored and referred to the 
next time the function of that input is needed, reducing the number of times the function is called. This is called 
memoization.


-Pure functions are more difficult to write in some situations.
"""
