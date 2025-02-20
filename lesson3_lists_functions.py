# Lesson 3: Lists and Functions
# Learn about storing multiple items and creating reusable code blocks

# 1. Lists
# Lists are ordered collections of items
fruits = ["apple", "banana", "orange", "grape"]
print("My fruit list:", fruits)

# Accessing list items (indexing starts at 0)
print("\nFirst fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Modifying lists
fruits.append("mango")  # Add to end
print("\nAfter adding mango:", fruits)

fruits.remove("banana")  # Remove specific item
print("After removing banana:", fruits)

# List operations
numbers = [1, 2, 3, 4, 5]
print("\nNumber list:", numbers)
print("List length:", len(numbers))
print("Sum of numbers:", sum(numbers))
print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))

# 2. Functions
# Functions are reusable blocks of code

# Simple function with no parameters
def say_hello():
    print("\nHello from a function!")

# Call the function
say_hello()

# Function with parameters
def greet(name):
    print(f"\nHello, {name}!")

greet("Alice")

# Function with return value
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print("\nResult of adding 5 and 3:", result)

# Function with multiple parameters and default value
def calculate_total(price, tax_rate=0.1):
    tax = price * tax_rate
    total = price + tax
    return total

purchase = calculate_total(100)  # Using default tax rate
print("\nTotal purchase with 10% tax:", purchase)

# 3. Combining Lists and Functions
def get_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

scores = [85, 92, 78, 90, 88]
average = get_average(scores)
print("\nAverage score:", average)

# 4. Challenge!
# Create a function that takes a list of numbers and returns only the even numbers
# Write your code below:
