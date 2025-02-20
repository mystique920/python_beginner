# Lesson 6: Lists

# 1. Creating a list
# A list is an ordered collection of items.
# Lists are created using square brackets [].

fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# Lists can contain items of different data types.
mixed_list = [1, "hello", 3.14, True]
print("Mixed list:", mixed_list)

# 2. Accessing elements
# Elements in a list are accessed using their index (position).
# The index starts at 0.

print("First fruit:", fruits[0])  # Access the first element (apple)
print("Second fruit:", fruits[1])  # Access the second element (banana)
print("Last fruit:", fruits[-1])  # Access the last element (cherry)

# 3. Modifying elements
# You can change the value of an element by assigning a new value to its index.

fruits[0] = "grape"
print("Modified fruits:", fruits)

# 4. Adding elements
# append(): Adds an element to the end of the list.
fruits.append("orange")
print("Fruits with orange:", fruits)

# insert(): Inserts an element at a specific index.
fruits.insert(1, "kiwi")
print("Fruits with kiwi:", fruits)

# 5. Removing elements
# remove(): Removes the first occurrence of a specific value.
fruits.remove("banana")
print("Fruits without banana:", fruits)

# pop(): Removes the element at a specific index and returns it.
removed_fruit = fruits.pop(2)
print("Removed fruit:", removed_fruit)
print("Fruits after pop:", fruits)

# 6. List slicing
# You can create a new list containing a portion of an existing list using slicing.

print("Sliced fruits:", fruits[1:3])  # Elements from index 1 (inclusive) to 3 (exclusive)

# 7. Challenge for you!
# Write a program that:
# - Creates a list of your favorite movies.
# - Prints the first and last movie in the list.
# - Adds a new movie to the end of the list.
# - Removes a movie from the list.
# - Prints the updated list.