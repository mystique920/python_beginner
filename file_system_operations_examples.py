import os
import shutil

# File System Operations Examples

# 1. Check if a path exists
# ------------------------
# Task: Check if a directory named 'example_dir' exists.
#      Print a message indicating whether it exists or not.
path_to_check = "example_dir"  # <--- TODO: Modify the path if needed

print("\n1. Check if path exists:")
if os.path.exists(path_to_check):
    print(f"   The path '{path_to_check}' exists.")
else:
    print(f"   The path '{path_to_check}' does not exist.")


# 2. Create directories
# ---------------------
# Task: Create a directory named 'new_directory'.
#      Handle the case where the directory already exists.
directory_to_create = "new_directory"  # <--- TODO: Modify the directory name if needed

print("\n2. Create directories:")
try:
    os.makedirs(directory_to_create, exist_ok=False)
    print(f"   Directory '{directory_to_create}' created successfully.")
except FileExistsError:
    print(f"   Directory '{directory_to_create}' already exists.")


# 3. Delete empty directories
# --------------------------
# Task: Create an empty directory named 'empty_dir' if it doesn't exist.
#      Then, try to delete it using os.rmdir().
#      Handle potential errors like FileNotFoundError or OSError (if not empty).
empty_directory_to_delete = "empty_dir" # <--- TODO: Modify the directory name if needed

print("\n3. Delete empty directories:")
if not os.path.exists(empty_directory_to_delete):
    os.makedirs(empty_directory_to_delete, exist_ok=True) # Create if not exists

try:
    os.rmdir(empty_directory_to_delete)
    print(f"   Directory '{empty_directory_to_delete}' removed successfully.")
except FileNotFoundError:
    print(f"   Directory '{empty_directory_to_delete}' not found.")
except OSError:
    print(f"   Directory '{empty_directory_to_delete}' is not empty and cannot be removed using os.rmdir().")


# 4. Delete non-empty directories (recursive delete - BE CAREFUL!)
# ---------------------------------------------------------------
# Task: Create a non-empty directory named 'non_empty_dir' with a subdirectory inside.
#      Then, try to delete it using shutil.rmtree().
#      BE VERY CAREFUL when using shutil.rmtree() as it permanently deletes directories and their contents.
non_empty_directory_to_delete = "non_empty_dir" # <--- TODO: Modify the directory name if needed
subdirectory_in_non_empty = os.path.join(non_empty_directory_to_delete, "subdir")

print("\n4. Delete non-empty directories (BE CAREFUL):")
if not os.path.exists(non_empty_directory_to_delete):
    os.makedirs(subdirectory_in_non_empty, exist_ok=True) # Create non-empty directory structure

try:
    shutil.rmtree(non_empty_directory_to_delete)
    print(f"   Directory '{non_empty_directory_to_delete}' and its contents removed successfully.")
except FileNotFoundError:
    print(f"   Directory '{non_empty_directory_to_delete}' not found.")


# 5. Rename files and directories
# -----------------------------
# Task: Create a directory named 'old_name' if it doesn't exist.
#      Then, rename it to 'new_name'.
#      Handle potential errors like FileNotFoundError or FileExistsError.
old_name = "old_name" # <--- TODO: Modify the old directory name if needed
new_name = "new_name" # <--- TODO: Modify the new directory name if needed

print("\n5. Rename files and directories:")
if not os.path.exists(old_name):
    os.makedirs(old_name, exist_ok=True) # Create if not exists

try:
    os.rename(old_name, new_name)
    print(f"   Renamed '{old_name}' to '{new_name}' successfully.")
except FileNotFoundError:
    print(f"   '{old_name}' not found.")
except FileExistsError:
    print(f"   '{new_name}' already exists.")


# 6. Move files and directories
# ---------------------------
# Task: Create a directory named 'source_dir' and another named 'destination_dir'.
#      Move 'source_dir' into 'destination_dir'.
#      Handle potential FileNotFoundError or FileExistsError.
source_path = "source_dir" # <--- TODO: Modify the source directory name if needed
destination_path = "destination_dir" # <--- TODO: Modify the destination directory name if needed

print("\n6. Move files and directories:")
if not os.path.exists(source_path):
    os.makedirs(source_path, exist_ok=True) # Create source if not exists
if not os.path.exists(destination_path):
    os.makedirs(destination_path, exist_ok=True) # Create destination if not exists


try:
    shutil.move(source_path, destination_path)
    print(f"   Moved '{source_path}' to '{destination_path}' successfully.")
except FileNotFoundError:
    print(f"   '{source_path}' not found.")
except FileExistsError:
    print(f"   '{destination_path}' already exists or '{source_path}' already exists in '{destination_path}'.")


print("\nFile system operations examples completed. Check the output and file system changes.")