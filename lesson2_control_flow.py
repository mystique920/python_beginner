# Lesson 2: Control Flow in Python
# In this lesson, we'll learn about decision-making in your code using if statements,
# repeating tasks with loops (while and for loops), and controlling loop behavior with break and continue.
# 1. If Statements
# If statements let your program perform different actions depending on conditions.
# For example, we can check if someone is old enough to vote.
age = 18  # The age of the person we're checking
print("Let's check if you can vote:")
if age >= 18:
    # If age is 18 or more, the condition becomes True.
    # This block of code runs when the condition is met.
    print("You can vote!")
else:
    # This block runs only when the condition in the if statement is False.
    print("Sorry, you're too young to vote.")

# Multiple conditions can be checked using "elif" (short for "else if").
score = 85  # A sample test score
print("\nChecking your grade:")
if score >= 90:
    # If the score is 90 or above, print an A grade message.
    print("A - Excellent!")
elif score >= 80:
    # If the above condition is False, but the score is 80 or above, then print a B grade message.
    print("B - Good job!")
elif score >= 70:
    # If both above conditions fail but the score is 70 or above, then print a C grade message.
    print("C - Satisfactory")
else:
    # If none of the above conditions are met (i.e., score is below 70), then one might need improvement.
    print("Need improvement")

# 2. While Loops
# A while loop repeatedly executes a block of code as long as its condition remains True.
print("\nCounting down:")
countdown = 5  # Start counting down from 5
while countdown > 0:
    # The condition "countdown > 0" is checked before each loop iteration.
    print(countdown)  # Print the current value of countdown
    countdown = countdown - 1  # Decrement countdown by 1 on each loop
print("Blast off!")  # This message prints after the loop finishes.
# 3. For Loops
# For loops are used for iterating over a sequence, such as a list or a range of numbers.
print("\nCounting up using for loop:")
# range(1, 6) generates the numbers 1 through 5.
for number in range(1, 6):
    print(number)  # Print each number as the loop iterates

# You can also loop through the characters of a string.
print("\nSpelling your name:")
name = "Python"  # The name to be spelled out letter by letter
for letter in name:
    print(letter)  # Each letter of the string is printed on a new line
# 4. Break and Continue
# The "break" statement exits the loop immediately.
print("\nDemonstrating break:")
for i in range(1, 11):
    # Loop over numbers from 1 to 10
    if i == 5:
        # When i equals 5, exit the loop immediately.
        break
    print(i)  # This prints numbers until i becomes 5

# The "continue" statement skips the current iteration and proceeds to the next one.
print("\nDemonstrating continue:")
for i in range(1, 6):
    if i == 3:
        # Skip printing the number 3.
        continue
    print(i)  # Print the number unless the iteration is skipped
# 5. Challenge!
# Create a loop that prints even numbers from 2 to 10.
# An even number is one that, when divided by 2, has no remainder.
print("\nPrinting even numbers from 2 to 10:")
for num in range(2, 11):  # range(2, 11) generates numbers from 2 to 10, inclusive.
    if num % 2 == 0:
        # If the remainder of num divided by 2 is 0, then num is even.
        print(num)
