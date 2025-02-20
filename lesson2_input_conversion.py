# Lesson 2: User Input and Type Conversion

# 1. Getting input from the user
# The input() function allows you to get text input from the user.
# The text inside the parentheses is the prompt that will be displayed to the user.
name = input("What is your name? ")
print("Hello, " + name + "!")

# 2. Converting input to different data types
# By default, input() returns a string (text).
# To use the input as a number, you need to convert it.

# Getting an integer (whole number)
age_str = input("What is your age? ")
age = int(age_str)  # Convert the string to an integer
print("You are", age, "years old.")

# Getting a float (decimal number)
height_str = input("What is your height in meters? ")
height = float(height_str)  # Convert the string to a float
print("Your height is", height, "meters.")

# 3. Error handling
# What happens if the user enters something that can't be converted?
# For example, if they enter "abc" when asked for their age?
# This will cause a ValueError!

# You can use a try-except block to handle potential errors:
try:
    number_str = input("Enter a number: ")
    number = int(number_str)
    print("You entered:", number)
except ValueError:
    print("That's not a valid number!")

# 4. Challenge for you!
# Write a program that asks the user for two numbers,
# converts them to integers, and then prints their sum.