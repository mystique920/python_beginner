# Useful Shell Scripting Commands

Here's a list of commonly used shell scripting commands with examples:

1.  **`echo`**:  Prints text to the console.

    ```bash
    echo "Hello, world!"
    ```

2.  **`ls`**: Lists files and directories.

    ```bash
    ls -l  # Lists files with details
    ls -a  # Lists all files, including hidden ones
    ```

3.  **`pwd`**: Prints the current working directory.

    ```bash
    pwd
    ```

4.  **`cd`**: Changes the current directory.

    ```bash
    cd /path/to/directory
    cd ..  # Goes up one directory
    ```

5.  **`mkdir`**: Creates a new directory.

    ```bash
    mkdir new_directory
    ```

6.  **`rm`**: Removes files or directories.

    ```bash
    rm file.txt  # Removes a file
    rm -r directory  # Removes a directory recursively
    ```

7.  **`cp`**: Copies files or directories.

    ```bash
    cp file.txt new_file.txt
    cp -r directory new_directory
    ```

8.  **`mv`**: Moves or renames files or directories.

    ```bash
    mv file.txt new_file.txt  # Renames a file
    mv file.txt /path/to/directory  # Moves a file
    ```

9.  **`cat`**: Displays the contents of a file.

    ```bash
    cat file.txt
    ```

10. **`head`**: Displays the first few lines of a file.

    ```bash
    head file.txt
    head -n 10 file.txt  # Displays the first 10 lines
    ```

11. **`tail`**: Displays the last few lines of a file.

    ```bash
    tail file.txt
    tail -n 10 file.txt  # Displays the last 10 lines
    tail -f file.txt  # Follows the file as it grows
    ```

12. **`grep`**: Searches for a pattern in a file.

    ```bash
    grep "pattern" file.txt
    grep -i "pattern" file.txt  # Case-insensitive search
    ```

13. **`find`**: Finds files based on various criteria.

    ```bash
    find . -name "file.txt"  # Finds files named "file.txt" in the current directory and its subdirectories
    find . -type d  # Finds all directories
    ```

14. **`chmod`**: Changes file permissions.

    ```bash
    chmod +x script.sh  # Makes a script executable
    ```

15. **`chown`**: Changes file ownership.

    ```bash
    chown user:group file.txt
    ```

16. **`ps`**: Displays running processes.

    ```bash
    ps aux  # Displays all processes
    ```

17. **`kill`**: Terminates a process.

    ```bash
    kill PID  # Replace PID with the process ID
    ```

18. **`top`**: Displays system resource usage.

    ```bash
    top
    ```

19. **`df`**: Displays disk space usage.

    ```bash
    df -h  # Displays disk space in human-readable format
    ```

20. **`du`**: Displays file space usage.

    ```bash
    du -sh directory  # Displays the total size of a directory in human-readable format
    ```

21. **`tar`**: Archives and extracts files.

    ```bash
    tar -czvf archive.tar.gz directory  # Creates a compressed archive
    tar -xzvf archive.tar.gz  # Extracts a compressed archive
    ```

22. **`wget`**: Downloads files from the internet.

    ```bash
    wget https://example.com/file.txt
    ```

23. **`curl`**: Transfers data from or to a server.

    ```bash
    curl https://example.com
    ```

24. **`sed`**: Stream editor for text manipulation.

    ```bash
    sed 's/old_text/new_text/g' file.txt  # Replaces all occurrences of "old_text" with "new_text" in file.txt
    ```

25. **`awk`**: Pattern scanning and processing language.

    ```bash
    awk '{print $1}' file.txt  # Prints the first column of each line in file.txt