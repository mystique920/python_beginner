# Lesson 17: Basic File System Operations

This lesson introduces you to basic file system operations in Python using the `os` module. Managing files and directories is a common task in programming, and the `os` module provides functions to interact with the operating system, including file system operations.

## Objectives

By the end of this lesson, you will be able to:

*   Import and use the `os` module.
*   Check if a file or directory exists using `os.path.exists()`.
*   Create directories using `os.makedirs()`.
*   Delete directories using `os.rmdir()` and `shutil.rmtree()`.
*   Rename files and directories using `os.rename()`.
*   Move files and directories using `shutil.move()`.

## 1. Importing the `os` Module

First, you need to import the `os` module to use its functions:

```python
import os
import shutil # for more advanced operations like removing non-empty directories and moving files
```

## 2. Checking if a File or Directory Exists

The `os.path.exists(path)` function checks if a path (file or directory) exists. It returns `True` if the path exists and `False` otherwise.

```python
path_to_check = "example_directory" # Replace with the path you want to check

if os.path.exists(path_to_check):
    print(f"The path '{path_to_check}' exists.")
else:
    print(f"The path '{path_to_check}' does not exist.")
```

## 3. Creating Directories

The `os.makedirs(path, exist_ok=False)` function creates a directory at the specified path.

*   `path`: The path of the directory to be created.
*   `exist_ok`: If `False` (default), it raises a `FileExistsError` if the target directory already exists. If `True`, it does not raise an error if the target directory exists.

```python
directory_to_create = "new_directory"

try:
    os.makedirs(directory_to_create, exist_ok=False)
    print(f"Directory '{directory_to_create}' created successfully.")
except FileExistsError:
    print(f"Directory '{directory_to_create}' already exists.")
```

To create nested directories, `os.makedirs()` will create all necessary intermediate directories.

## 4. Deleting Directories

*   **Deleting Empty Directories**:
    The `os.rmdir(path)` function removes an empty directory. It raises an `OSError` if the directory is not empty.

    ```python
    directory_to_delete = "empty_directory" # Make sure this directory is empty

    try:
        os.rmdir(directory_to_delete)
        print(f"Directory '{directory_to_delete}' removed successfully.")
    except FileNotFoundError:
        print(f"Directory '{directory_to_delete}' not found.")
    except OSError:
        print(f"Directory '{directory_to_delete}' is not empty and cannot be removed using os.rmdir().")
    ```

*   **Deleting Non-Empty Directories**:
    To delete a directory and all its contents (files and subdirectories), you can use `shutil.rmtree(path)`. **Be very careful when using this function as it permanently deletes directories and their contents.**

    ```python
    directory_to_delete_recursive = "non_empty_directory" # Be CAREFUL with this!

    try:
        shutil.rmtree(directory_to_delete_recursive)
        print(f"Directory '{directory_to_delete_recursive}' and its contents removed successfully.")
    except FileNotFoundError:
        print(f"Directory '{directory_to_delete_recursive}' not found.")
    ```

## 5. Renaming Files and Directories

The `os.rename(src, dst)` function renames a file or directory from `src` to `dst`.

```python
old_name = "old_directory_name"
new_name = "new_directory_name"

try:
    os.rename(old_name, new_name)
    print(f"Renamed '{old_name}' to '{new_name}' successfully.")
except FileNotFoundError:
    print(f"'{old_name}' not found.")
except FileExistsError:
    print(f"'{new_name}' already exists.")
```

This function can be used for both files and directories.

## 6. Moving Files and Directories

The `shutil.move(src, dst)` function moves a file or directory from `src` to `dst`. It can handle moving files across file systems.

```python
source_path = "source_directory"
destination_path = "destination_directory"

try:
    shutil.move(source_path, destination_path)
    print(f"Moved '{source_path}' to '{destination_path}' successfully.")
except FileNotFoundError:
    print(f"'{source_path}' not found.")
except FileExistsError:
    print(f"'{destination_path}' already exists.")
```

If the destination is an existing directory, the source will be moved inside the destination directory.

## Example Code

Here is an example that demonstrates some of these operations:

```python
import os
import shutil

# Check if a directory exists
directory_name = "test_dir"
if not os.path.exists(directory_name):
    # Create a directory
    os.makedirs(directory_name)
    print(f"Directory '{directory_name}' created.")
else:
    print(f"Directory '{directory_name}' already exists.")

# Rename the directory
new_directory_name = "test_dir_renamed"
try:
    os.rename(directory_name, new_directory_name)
    print(f"Directory '{directory_name}' renamed to '{new_directory_name}'.")
    directory_name = new_directory_name # Update directory_name
except FileNotFoundError:
    print(f"Directory '{directory_name}' not found for renaming.")

# Create a subdirectory
subdirectory_name = os.path.join(directory_name, "subdir") # Use os.path.join for path safety
os.makedirs(subdirectory_name, exist_ok=True)
print(f"Subdirectory '{subdirectory_name}' created.")

# Move the subdirectory
moved_subdirectory_name = "moved_subdir"
shutil.move(subdirectory_name, moved_subdirectory_name)
print(f"Subdirectory '{subdirectory_name}' moved to '{moved_subdirectory_name}'.")


# List contents of the directory (optional, covered in other lessons if needed)
print(f"Contents of '{directory_name}': {os.listdir(directory_name)}")


# Clean up: remove the directory and its contents (BE CAREFUL!)
try:
    shutil.rmtree(directory_name) # Removes the renamed directory
    print(f"Directory '{directory_name}' and its contents removed.")
except FileNotFoundError:
    print(f"Directory '{directory_name}' not found for removal.")
except OSError as e:
    print(f"Error removing directory '{directory_name}': {e}")


# Clean up moved subdirectory
try:
    os.rmdir(moved_subdirectory_name) # Removes the moved subdirectory (if empty)
    print(f"Directory '{moved_subdirectory_name}' removed.")
except FileNotFoundError:
    print(f"Directory '{moved_subdirectory_name}' not found for removal.")
except OSError as e:
    print(f"Error removing directory '{moved_subdirectory_name}': {e}")


print("File system operations example completed.")
```

**Important Notes:**

*   Always be cautious when deleting files and directories, especially when using `shutil.rmtree()`. Double-check paths to avoid accidental data loss.
*   Use `os.path.join()` to construct paths to ensure cross-platform compatibility.
*   Error handling (using `try...except` blocks) is important when performing file system operations, as operations can fail due to various reasons (e.g., permissions, file not found, directory not empty).

This lesson provides a basic introduction to file system operations. You can explore more advanced features of the `os` and `shutil` modules in the Python documentation.