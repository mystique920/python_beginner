# Virtual Environment Examples

# This file provides examples of how to create, activate, and manage virtual environments in Python using VS Code.
# These examples are tailored for macOS users.

# 1. Creating a virtual environment using venv (recommended)
# Open your VS Code terminal (View -> Terminal).
# Navigate to your project directory using the 'cd' command.
# Run the following command to create a virtual environment named "myenv":
#
# python3 -m venv myenv
#
# This will create a new directory named "myenv" containing the virtual environment files.

# 2. Creating a virtual environment using virtualenv (if venv is not available)
# If you don't have venv, you can use virtualenv. First, install it using the VS Code terminal:
#
# pip install virtualenv
#
# Then, create a virtual environment:
#
# virtualenv myenv

# 3. Activating the virtual environment in VS Code
# VS Code will usually detect the virtual environment automatically and prompt you to select it.
# If not, you can manually select the virtual environment by:
#   - Opening the Command Palette (View -> Command Palette or Cmd+Shift+P).
#   - Typing "Python: Select Interpreter" and pressing Enter.
#   - Choosing the Python interpreter located inside your virtual environment (e.g., ./myenv/bin/python).
#
# After selecting the virtual environment, VS Code will use it for running your Python code.

# 4. Activating the virtual environment using the VS Code terminal (alternative)
# You can also activate the virtual environment directly in the VS Code terminal:
#
# source myenv/bin/activate
#
# After activating, you should see the environment name in parentheses in your terminal prompt, like this:
#
# (myenv)

# 5. Installing packages in the virtual environment
# Once the environment is activated, you can install packages using pip in the VS Code terminal:
#
# pip install requests
#
# This will install the "requests" package and its dependencies into the virtual environment.

# 6. Deactivating the virtual environment
# When you're finished working in the virtual environment, you can deactivate it using the VS Code terminal:
#
# deactivate
#
# This will return you to your system's default Python environment.

# 7. Freezing dependencies
# To save the list of packages installed in your virtual environment, you can use pip freeze in the VS Code terminal:
#
# pip freeze > requirements.txt
#
# This will create a file named "requirements.txt" containing the list of packages and their versions.
# You can use this file to recreate the environment on another machine or share it with others.
#
# It is important to include the 'requirements.txt' file in your project's version control system (e.g., Git)
# so that others can easily recreate the environment.

# 8. Installing from requirements.txt
# To install packages from a requirements.txt file using the VS Code terminal:
#
# pip install -r requirements.txt

# 9. Deleting a virtual environment
# To delete a virtual environment, simply remove the environment directory using the VS Code terminal:
#
# rm -rf myenv
#
# WARNING: This will permanently delete the virtual environment and all its contents.