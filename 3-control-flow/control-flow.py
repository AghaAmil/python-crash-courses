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
