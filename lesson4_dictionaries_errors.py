# Lesson 4: Dictionaries and Error Handling
# Learn about key-value pairs and handling errors in Python

# 1. Dictionaries
# Dictionaries store key-value pairs
student = {
    "name": "John",
    "age": 20,
    "grades": [85, 90, 88],
    "active": True
}

# Accessing dictionary values
print("Student name:", student["name"])
print("Student age:", student["age"])

# Adding and modifying dictionary items
student["email"] = "john@example.com"  # Add new key-value pair
student["age"] = 21  # Modify existing value

# Dictionary methods
print("\nDictionary keys:", student.keys())
print("Dictionary values:", student.values())

# Checking if key exists
if "email" in student:
    print("\nEmail exists:", student["email"])

# 2. Error Handling
# Try-except blocks help handle errors gracefully

# Division by zero error
print("\nHandling division by zero:")
try:
    result = 10 / 0
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Key error in dictionary
print("\nHandling dictionary key error:")
try:
    print(student["phone"])  # 'phone' key doesn't exist
except KeyError:
    print("Error: Phone number not found in student data!")

# Multiple error types
def safe_divide(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero!"
    except TypeError:
        return "Please provide numbers only!"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

print("\nTesting safe division:")
print("10 / 2 =", safe_divide(10, 2))
print("10 / 0 =", safe_divide(10, 0))
print('10 / "2" =', safe_divide(10, "2"))

# 3. Combining Dictionaries and Error Handling
def get_student_grade(student_dict, subject):
    try:
        grades = student_dict.get("grades", [])
        if not grades:
            raise ValueError("No grades available")
        return sum(grades) / len(grades)
    except ValueError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

print("\nCalculating student average:")
print("Average grade:", get_student_grade(student, "math"))

# 4. Challenge!
# Create a dictionary for a shopping cart with items and prices
# Write a function that calculates the total cost with error handling
# Write your code below:
