# Lesson 9: Modules and Libraries

# 1. Importing a module
# A module is a file containing Python code that you can use in your program.
# Modules are imported using the 'import' statement.

import math  # Import the 'math' module

# 2. Using functions from a module
# To use a function from a module, you need to specify the module name followed by a dot (.) and the function name.

print("Square root of 16:", math.sqrt(16))  # Use the sqrt() function from the math module
print("Pi:", math.pi)  # Access the value of pi from the math module

# 3. Common modules
# Python has many built-in modules that provide useful functions.

# The 'random' module provides functions for generating random numbers.
import random

print("Random number between 1 and 10:", random.randint(1, 10))

# The 'datetime' module provides functions for working with dates and times.
import datetime

now = datetime.datetime.now()
print("Current date and time:", now)

# 4. Aliasing modules
# You can give a module a shorter name using the 'as' keyword.

import math as m

print("Square root of 25:", m.sqrt(25))

# 5. Importing specific functions
# You can import specific functions from a module using the 'from ... import ...' statement.

from math import sqrt, pi

print("Square root of 36:", sqrt(36))
print("Pi:", pi)

# 6. Challenge for you!
# Write a program that:
# - Uses the 'random' module to generate a random number between 1 and 100.
# - Asks the user to guess the number.
# - Tells the user whether their guess is too high, too low, or correct.