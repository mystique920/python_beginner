# Lesson 8: Dictionaries

# 1. Creating a dictionary
# A dictionary is a collection of key-value pairs.
# Dictionaries are created using curly braces {}.

student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}
print("Student:", student)

# 2. Accessing values
# Values in a dictionary are accessed using their keys.

print("Name:", student["name"])  # Access the value associated with the key "name"
print("Age:", student["age"])  # Access the value associated with the key "age"

# 3. Modifying values
# You can change the value associated with a key by assigning a new value to it.

student["age"] = 21
print("Updated student:", student)

# 4. Adding key-value pairs
# You can add new key-value pairs to a dictionary by assigning a value to a new key.

student["gpa"] = 3.8
print("Student with GPA:", student)

# 5. Removing key-value pairs
# You can remove a key-value pair from a dictionary using the 'del' keyword.

del student["major"]
print("Student without major:", student)

# 6. Dictionary methods
# keys(): Returns a list of all the keys in the dictionary.
print("Keys:", student.keys())

# values(): Returns a list of all the values in the dictionary.
print("Values:", student.values())

# items(): Returns a list of all the key-value pairs in the dictionary as tuples.
print("Items:", student.items())

# 7. Challenge for you!
# Write a program that:
# - Creates a dictionary to store information about a book (title, author, year).
# - Prints the book's title and author.
# - Adds a new key-value pair to store the book's genre.
# - Removes the book's year.
# - Prints the updated dictionary.