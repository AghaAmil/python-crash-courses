# creating a function
def func_print():
    print('This is a function that prints something')


func_print()

# blank space
print('')


# concatenation function
def add(number1: int, number2: int) -> int:
    # add them together
    num3 = number1 + number2

    return num3


# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")

# blank space
print('')


# is_prime() number

def is_prime(input_num):
    if input_num > 1:
        for i in range(2, input_num):
            if input_num % i == 0:
                return 'is not a prime number'
                break
            else:
                return 'is a prime number'
    else:
        return 'Invalid input number'


print(f'The number 19 {is_prime(19)}')
print(f'The number 19 {is_prime(50)}')
print(f'The number 19 {is_prime(0)}')

# blank space
print('')


# A simple Python function to check
# whether x is even or odd
def odd_even(x):
    if x % 2 == 0:
        return 'even number'
    else:
        return 'odd number'


print(f'The number 10 is {odd_even(10)}')
print(f'The number 21 is {odd_even(21)}')
print(f'The number 40 is {odd_even(40)}')

# blank space
print('')


# positional arguments
def nameAge(name, age):
    print(f'User\'s name is: {name}\nUser\'s age is: {age}')


print('New User')
print('--------')
nameAge('Amirhossein Moravveji', 30)

# blank space
print('')


# Here x is a new reference to same list lst
def myFun(x):
    x[0] = 20


# Driver Code (Note that lst is modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]

print(lst)
myFun(lst)
print(lst)

# blank space
print('')


# Python program to illustrate *args for a variable number of arguments
def my_func_1(*args):
    for word in args:
        print(word)


my_func_1('my', 'name', 'is', 'Amirhossein', 'Moravveji')

# blank space
print('')


# Another example
def my_func_2(arg1, *args):
    print(f'This is the first argument: {arg1}')

    for words in args:
        print(f'This is the rest of the arguments: {words}')


my_func_2('hello', 'world', 'of', 'python', '!')

# blank space
print('')
