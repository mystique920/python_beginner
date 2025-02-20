# Lesson 5: Working with Files and Modules
# Learn about reading/writing files and using Python modules

# 1. File Operations
# Writing to a file
print("Writing to a file...")
with open("example.txt", "w") as file:
    file.write("Hello from Python!\n")
    file.write("This is line 2\n")
    file.write("This is line 3\n")

# Reading from a file
print("\nReading from the file:")
try:
    with open("example.txt", "r") as file:
        content = file.read()
        print("File contents:")
        print(content)
except FileNotFoundError:
    print("Error: File not found!")

# Reading line by line
print("\nReading line by line:")
try:
    with open("example.txt", "r") as file:
        for line_number, line in enumerate(file, 1):
            print(f"Line {line_number}: {line.strip()}")
except FileNotFoundError:
    print("Error: File not found!")

# 2. Working with Modules
# Built-in modules
import random
import math
import datetime

# Using the random module
print("\nRandom number between 1 and 10:", random.randint(1, 10))
colors = ["red", "green", "blue", "yellow"]
print("Random color:", random.choice(colors))

# Using the math module
print("\nMath operations:")
print("Square root of 16:", math.sqrt(16))
print("Pi:", math.pi)
print("Ceiling of 4.3:", math.ceil(4.3))
print("Floor of 4.3:", math.floor(4.3))

# Using the datetime module
current_time = datetime.datetime.now()
print("\nCurrent date and time:", current_time)
print("Year:", current_time.year)
print("Month:", current_time.month)
print("Day:", current_time.day)

# 3. Creating a Custom Module
# Note: This would normally be in a separate file
# Here's how you would use it if it was in 'mymath.py':
"""
def double(n):
    return n * 2

def square(n):
    return n * n
"""

# Using your custom module would look like this:
# import mymath
# print(mymath.double(5))
# print(mymath.square(4))

# 4. Combining Files and Modules
def log_activity(activity):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("activity_log.txt", "a") as file:
            file.write(f"{timestamp}: {activity}\n")
        return True
    except Exception as e:
        print(f"Error logging activity: {e}")
        return False

# Log some activities
log_activity("Program started")
log_activity("Generated random number: " + str(random.randint(1, 100)))
log_activity("Program ended")

# 5. Challenge!
# Create a program that:
# 1. Reads numbers from a file (one number per line)
# 2. Calculates their average using the math module
# 3. Writes the result to a new file
# Write your code below:
