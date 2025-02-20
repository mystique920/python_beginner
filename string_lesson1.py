# Lesson 1: Advanced String Operations

# String slicing and indexing
# Accessing individual characters
string = "Hello, World!"
print("Original string:", string)
print("First character:", string[0])
print("Last character:", string[-1])

# Slicing a string
print("First 5 characters:", string[0:5])
print("Characters from index 7 to 11:", string[7:12])
print("Every other character:", string[::2])
print("Reverse the string:", string[::-1])

# String methods: strip(), lower(), upper(), replace(), split(), join()
string = "   Python is fun!   "

# strip() - Remove leading/trailing whitespace
stripped_string = string.strip()
print("\nStripped string:", stripped_string)

# lower() - Convert to lowercase
lower_string = stripped_string.lower()
print("Lowercase string:", lower_string)

# upper() - Convert to uppercase
upper_string = stripped_string.upper()
print("Uppercase string:", upper_string)

# replace() - Replace a substring
replaced_string = stripped_string.replace("fun", "awesome")
print("Replaced string:", replaced_string)

# split() - Split the string into a list of substrings
split_string = stripped_string.split()
print("Split string:", split_string)

# join() - Join a list of strings into a single string
joined_string = " ".join(split_string)
print("Joined string:", joined_string)

# String formatting: % operator, .format() method, f-strings
name = "Alice"
age = 30

# % operator (old style)
print("\nUsing % operator: Name: %s, Age: %d" % (name, age))

# .format() method
print("Using .format() method: Name: {}, Age: {}".format(name, age))

# f-strings (Python 3.6+)
print(f"Using f-strings: Name: {name}, Age: {age}")

# Additional examples
number = 123.456
print(f"Formatted number: {number:.2f}") # Keep 2 decimal places