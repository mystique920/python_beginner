# Lesson 7: Functions

# 1. Defining a function
# A function is a reusable block of code.
# Functions are defined using the 'def' keyword.

def greet(name):
    """This function greets the person passed in as a parameter."""
    print("Hello, " + name + "!")

# 2. Calling a function
# To use a function, you need to call it.

greet("Alice")  # Call the greet function with the argument "Alice"
greet("Bob")  # Call the greet function with the argument "Bob"

# 3. Function parameters
# Functions can take parameters as input.
# Parameters are variables that are passed to the function when it is called.

def add(x, y):
    """This function adds two numbers and returns the sum."""
    sum = x + y
    return sum

# 4. Return values
# Functions can return a value using the 'return' statement.

result = add(5, 3)  # Call the add function with arguments 5 and 3
print("The sum is:", result)  # Print the returned value

# 5. Scope of variables
# Variables defined inside a function are local to that function.
# They cannot be accessed from outside the function.

def my_function():
    local_variable = 10
    print("Inside the function:", local_variable)

my_function()
# print(local_variable)  # This would cause an error because local_variable is not defined outside the function

# 6. Challenge for you!
# Write a function that:
# - Takes two numbers as input.
# - Returns the product of the two numbers.
# - Prints the result.