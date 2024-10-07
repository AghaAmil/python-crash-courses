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

"""
Lesson 2 - Lambdas
"""


def polynomial(x):
    return x ** 2 + 5 * x + 4


print('')
print(polynomial(5))

# Lambdas
print((lambda x: x ** 2 + 5 * x + 4)(-4))

"""
Lesson 3 - Map & Filter
"""

# map
print('\nmap')

list_of_numbers = [11, 22, 33, 44, 55, 66, 77]
print(list_of_numbers)

print(list(map(lambda x: x ** 2 - 6, list_of_numbers)))

# filter
print('\nfilter')

list_of_numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_of_numbers1)

print(list(filter(lambda x: x % 2 == 0, list_of_numbers1)))

"""
Lesson 4 - Generators
"""


def generator():
    i = 5
    while i > 0:
        yield i
        i -= 1


for i in generator():
    print(i)

"""
The yield statement is used to define a generator, replacing the return of a function to provide a result to its 
caller without destroying local variables.

Due to the fact that they yield one item at a time, generators don't have the memory restrictions of lists. 
In fact, they can be infinite!
"""


def even_num_func(x):
    for num in range(x):
        if num % 2 == 0:
            yield num


print(list(even_num_func(25)))


# New trick it words
def makeWord():
    word = ''
    for char in 'amirhossein':
        word += char
        yield word


print(list(makeWord()))

"""
Lesson 5 - Decorators
"""


def decor(func):
    def wrap():
        print("============")
        func()
        print("============")

    return wrap


def hello_world():
    print('Hello World!')


decorated = decor(hello_world)
decorated()


# new pattern
def decory(func):
    def greeting(name, surname):
        print('******** Apple INC ********')
        print('***************************')
        print('')
        func(name, surname)
        print('')
        print('***************************')
        print('****** Enjoy Shotory ******')

    return greeting


@decory
def User(name, surname):
    print('Welcome to our company ' + name + ' ' + surname + '. Have a good day')


worker_name = input('Enter your first name: ')
worker_family_name = input('Enter your family name: ')
print('')

User(worker_name, worker_family_name)

"""
Lesson 6 - Recursion
"""


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(5))
"""
The base case acts as the exit condition of the recursion.
Not adding a base case results in infinite function calls, crashing the program.
"""

"""
How the code works:

x = 5 --> factorial(5)          return --> 5 * factorial(4)             calculation = 5 * 24 = 120      ^
next ---> factorial(4)          return --> 4 * factorial(3)             calculation = 4 * 6 = 24        ^
next ---> factorial(3)          return --> 3 * factorial(2)             calculation = 3 * 2 = 6         ^
next ---> factorial(2)          return --> 2 * factorial(1) = 1         calculation = 2 * 1 = 2         ^
"""


def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x - 1)


def is_odd(x):
    return not is_even(x)


print(is_odd(17))
print(is_even(23))

"""
Lesson 7 - *args and **kwargs
"""


def printer(x, y, *args, **kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)


printer(2, 3, 4, 5, 6, 7, a=8, b=9)
