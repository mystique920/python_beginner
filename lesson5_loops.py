# Lesson 5: Loops (for and while)

# 1. The 'for' loop
# The 'for' loop is used to iterate over a sequence (e.g., a list, string, or range).

# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating over a string
message = "Hello"
for char in message:
    print(char)

# 2. The 'range()' function
# The 'range()' function generates a sequence of numbers.

# Printing numbers from 0 to 4
for i in range(5):
    print(i)

# Printing numbers from 2 to 5
for i in range(2, 6):
    print(i)

# Printing even numbers from 0 to 10
for i in range(0, 11, 2):
    print(i)

# 3. The 'while' loop
# The 'while' loop repeats a block of code as long as a condition is True.

count = 0
while count < 5:
    print(count)
    count += 1  # Increment count to avoid an infinite loop

# 4. 'break' and 'continue' statements
# The 'break' statement exits the loop prematurely.
# The 'continue' statement skips the current iteration and continues to the next.

for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)

# 5. Challenge for you!
# Write a program that:
# - Asks the user for a number.
# - Uses a 'for' loop to print the multiplication table for that number (from 1 to 10).