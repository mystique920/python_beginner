# Lesson: Debugging in Python

# 1. Using the VS Code Debugger

# The VS Code debugger is a powerful tool for finding and fixing errors in your code.
# Here's how to use it:

# - Set breakpoints: Click in the left margin (gutter) next to a line number to set a breakpoint.
#   Execution will pause at this line when you run the debugger.
# - Start debugging: Press F5 or go to Run > Start Debugging.
# - Step through your code:
#    - Step Over (F10): Executes the current line and moves to the next.
#    - Step Into (F11): If the current line is a function call, steps into the function.
#    - Step Out (Shift+F11): Executes the remaining lines in the current function and returns to the caller.
#    - Continue (F5): Resumes execution until the next breakpoint.
# - Inspect variables: Use the "Variables" pane to see the values of variables at different points in your code.
# - Watch expressions: Use the "Watch" pane to track the values of specific expressions.
# - Use the debug console: The "Debug Console" allows you to evaluate expressions and interact with your code while debugging.

# Example:
def calculate_sum(a, b):
    result = a + b  # Set a breakpoint here
    return result

x = 5
y = 10
sum_result = calculate_sum(x, y)
print(f"The sum is: {sum_result}")

# 2. Understanding Common Error Messages

# Python provides informative error messages when something goes wrong. Here are some common ones:

# - **SyntaxError:**  This is like a grammar mistake in Python. It means Python doesn't understand the structure of your code.
#   **Example:**  `print("Hello"` (missing a closing quote or parenthesis) or incorrect indentation.
#   **Tip:** VS Code usually helps spot these *before* you even run the code! Look for red squiggly lines.
# - **NameError:**  Python is saying "I don't know what you're talking about!". It means you're using a name (usually a variable) that hasn't been created yet.
#   **Example:**  `print(my_variable)` if you forgot to write `my_variable = 10` earlier.
#   **Tip:**  Make sure you create variables before you use them.
# - **TypeError:**  You're trying to do something that Python thinks is the wrong *type* of action for the data.
#   **Example:**  `"hello" + 5` (you can't directly add text and a number).
#   **Tip:**  Think about the *types* of data you're using (numbers, text, lists, etc.) and if the action makes sense for those types.
# - **IndexError: list index out of range:**  This is a list problem! It means you're trying to get an item from a list using a number (index) that's not valid. Imagine a list with 3 items; the valid indexes are 0, 1, and 2.
#   **Example:** `my_list = [10, 20, 30]; print(my_list[5])` (index 5 is too big).
#   **Tip:**  Remember lists start at index 0, and go up to *length of list - 1*.
# - **KeyError:** Like `IndexError`, but for dictionaries (which use *keys* instead of indexes). It means you're asking for a key that's not in the dictionary.
#   **Example:** `my_dict = {"name": "Alice"}; print(my_dict["age"])` (the key "age" doesn't exist).
#   **Tip:**  Make sure you're using the correct key, and that the key exists in the dictionary.
# - **ValueError:**  Python is saying "I understand *what* you want to do, but the *value* you gave me isn't right."
#   **Example:** `int("hello")` (you can't turn the text "hello" into a number).
#   **Tip:**  Check the *values* you're giving to functions, and if they make sense for what the function is supposed to do.
# - **AttributeError:**  You're trying to use a "tool" (method or attribute) that doesn't belong to the "object" you're working with.
#   **Example:** `"hello".append("!")` (strings don't have an `append` "tool", lists do).
#   **Tip:**  Make sure you're using the right "tools" for the type of data you have.

# Example (SyntaxError):
# print("Hello"  # Missing closing parenthesis

# Example (NameError):
# print(my_variable)  # my_variable is not defined

# Example (TypeError):
# result = "5" + 10

# 3. Using print() Statements for Debugging

# A simple but effective debugging technique is to insert print() statements to display the values of variables
# or track the flow of execution.

# Example:
def my_function(data):
    print(f"Input data: {data}")  # Debugging print statement
    processed_data = [x * 2 for x in data]
    print(f"Processed data: {processed_data}") # Debugging print statement
    return processed_data

my_list = [1, 2, 3]
result = my_function(my_list)
print(f"Result: {result}")

# 4. Challenge
# Debug the following code:

# def calculate_average(numbers)
#   sum = 0
#   for number in numbers
#       sum += number
#    average = sum / len(numbers)
#   return average

# my_numbers = [1, 2, 3, 4, 5]
# result = calculate_average(my_numbers)
# print(f"Average: {result}")

# Solution to challenge
def calculate_average(numbers):
  sum_of_numbers = 0
  for number in numbers:
      sum_of_numbers += number
  average = sum_of_numbers / len(numbers)
  return average