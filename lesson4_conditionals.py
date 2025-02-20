# Lesson 4: Conditional Statements (if/else)

# 1. The 'if' statement
# The 'if' statement allows you to execute code only if a certain condition is True.

age = 20

if age >= 18:
    print("You are an adult.")  # This will be printed because age is greater than or equal to 18

# 2. The 'else' statement
# The 'else' statement provides an alternative block of code to execute if the 'if' condition is False.

age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")  # This will be printed because age is less than 18

# 3. The 'elif' statement
# The 'elif' (else if) statement allows you to check multiple conditions in a sequence.

score = 75

if score >= 90:
    print("Excellent!")
elif score >= 80:
    print("Very good!")
elif score >= 70:
    print("Good!")  # This will be printed because score is between 70 and 79
else:
    print("Needs improvement.")

# 4. Nested 'if' statements
# You can put 'if' statements inside other 'if' statements to create more complex logic.

temperature = 25
raining = True

if temperature > 20:
    print("It's warm.")
    if not raining:
        print("It's a nice day!")
    else:
        print("But it's raining.")
else:
    print("It's cold.")

# 5. Challenge for you!
# Write a program that asks the user for a number and then:
# - Prints "Positive" if the number is greater than 0.
# - Prints "Negative" if the number is less than 0.
# - Prints "Zero" if the number is equal to 0.