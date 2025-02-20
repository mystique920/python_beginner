# Lesson 3: Basic Operators

# 1. Arithmetic Operators
# These operators are used for basic math calculations.

x = 10
y = 5

print("x =", x)
print("y =", y)

print("Addition (x + y):", x + y)  # Adds x and y
print("Subtraction (x - y):", x - y)  # Subtracts y from x
print("Multiplication (x * y):", x * y)  # Multiplies x and y
print("Division (x / y):", x / y)  # Divides x by y (result is a float)
print("Floor Division (x // y):", x // y)  # Divides x by y (result is an integer, discarding the decimal)
print("Modulo (x % y):", x % y)  # Returns the remainder of the division
print("Exponentiation (x ** y):", x ** y)  # Raises x to the power of y

# 2. Comparison Operators
# These operators are used to compare values.
# They return a Boolean (True or False).

print("\nComparison Operators:")
print("x == y:", x == y)  # Equal to
print("x != y:", x != y)  # Not equal to
print("x > y:", x > y)  # Greater than
print("x < y:", x < y)  # Less than
print("x >= y:", x >= y)  # Greater than or equal to
print("x <= y:", x <= y)  # Less than or equal to

# 3. Logical Operators
# These operators are used to combine or modify Boolean values.

print("\nLogical Operators:")
a = True
b = False

print("a =", a)
print("b =", b)

print("a and b:", a and b)  # Returns True if both a and b are True
print("a or b:", a or b)  # Returns True if either a or b is True
print("not a:", not a)  # Returns the opposite of a

# 4. Challenge for you!
# Write a program that asks the user for two numbers and then:
# - Prints whether the first number is greater than, less than, or equal to the second number.
# - Prints whether both numbers are positive.