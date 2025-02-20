# Advanced Strings and Data Types in Python

# 1. String Slicing and Indexing
text = "Python is a powerful language"
print("Original text:", text)
print("First character:", text[0])
print("Last character:", text[-1])
print("First 6 characters:", text[:6])
print("Characters from index 7:", text[7:])
print("Characters from index 2 to 10:", text[2:11])

# 2. String Methods
text = "   Python is Awesome   "
print("\nOriginal text:", text)
print("Stripped text:", text.strip())
print("Lowercase text:", text.lower())
print("Uppercase text:", text.upper())
print("Replaced text:", text.replace("Awesome", "Great"))
print("Split text:", text.split())

text = "apple,banana,cherry"
print("\nOriginal text:", text)
print("Joined text:", "-".join(text.split(",")))

# 3. String Formatting
name = "Alice"
age = 30
print("\nString formatting using % operator: %s is %d years old" % (name, age))
print("String formatting using .format() method: {} is {} years old".format(name, age))

# 4. F-strings (Formatted String Literals)
# F-strings provide a concise and readable way to embed expressions inside string literals for formatting.
name = "Bob"
age = 25
print(f"\nF-string: {name} is {age} years old")

# You can also include expressions inside f-strings
x = 10
y = 5
print(f"F-string with expression: The sum of {x} and {y} is {x + y}")

# 5. Regular Expressions
import re

text = "The quick brown fox jumps over the lazy dog"
pattern = "fox"
match = re.search(pattern, text)

if match:
    print("\nRegular expression match found:", match.group())

# 6. Named Tuples
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print("\nNamed tuple:", p)
print("X coordinate:", p.x)
print("Y coordinate:", p.y)

# 7. Counters
from collections import Counter

numbers = [1, 2, 3, 1, 2, 1, 4, 5, 1]
count = Counter(numbers)
print("\nCounter:", count)
print("Count of 1:", count[1])

# 8. Ordered Dictionaries
from collections import OrderedDict

ordered_dict = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
print("\nOrdered dictionary:", ordered_dict)