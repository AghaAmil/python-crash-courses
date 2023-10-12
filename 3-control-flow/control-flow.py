"""
Lesson 1 - Control Flow
Lesson Takeaways

- You use sequencing, iteration and selection to control the flow of instructions
- An algorithm is a set of step-by-step instructions to complete a task
- Algorithms can be represented in different ways
"""

# The practices already mentioned in the sololearn website
# Nothing to add

"""
Lesson 4 - for loop
Lesson Takeaways
 
- you can implement iteration into your programs with the for loop
- the initial loop statement must be followed by a colon : symbol
- the code that gets repeated must be indented
"""

# Let write some basic examples
print('first for loop example')

for i in range(5):
    print('I have learnt for loop in python :)')

print('Lets print 0 to 10 numbers:')

for num in range(11):
    print('This is number: ' + str(num))

# Something cool I have designed
itr = int(input('Input a positive integer to display a sequence of numbers from zero to the input value.'))

for num1 in range(itr + 1):
    print(num1)

"""
Lesson 2 - While Loop
Lesson Takeaways
 
- you can apply iteration to your programs with the while loop
- counters keep track of the number of iterations and avoid infinite loops
- indentation and the colon : symbol are required for the code to run
"""
# While Loop Example
print('For example, a ticket seller at a theater will repeatedly sell tickets until all seats have been occupied')

seat = 24

while seat > 0:
    print('Cinema is selling tickets. Ticket Number is #' + str(seat))
    seat = seat - 1

"""
Lesson 2 - More On Iteration
Lesson Takeaways
 
- for loops are used when the number of iterations is known
- you can solve real problems by combining comparison operations and iterations
"""

# more on comparison operation...
print(5 == 5)  # is 5 equal to 5?
print(5 == 7)  # is 5 equal to 7?
print(5 != 7)  # is 5 different from 7?
print(5 != 5)  # is 5 different from 5?
print(5 <= 5)  # is 5 less than or equal to 5?
print(5 >= 5)  # is 5 greater than or equal to 5?

# a real world example
password = 'secretP@ss'
entered_pass = input("Enter the system password: ")

while entered_pass != password:
    entered_pass = input("Password is Wrong!! Try Again: ")

print('Password is correct - Access Granted')
