# Exception Handling Using try...except
try:
    numerator = 10
    denominator = 0

    result = numerator / denominator

except ZeroDivisionError:
    print("Division by zero cannot be possible")

# Catching Specific Exceptions in Python
try:
    even_numbers = [2, 4, 6, 8]
    print(even_numbers[5])

except IndexError:
    print("Index Out of Bound.")
except ZeroDivisionError:
    print("Division by zero cannot be possible")

# Python try with else clause
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1 / num
    print(reciprocal)

# Python try...finally
try:
    numerator = 10
    denominator = 0

    result = numerator / denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")

finally:
    print("This is finally block.")
