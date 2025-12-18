# File Handling in Python

Python provides built-in functions for file handling, allowing you to create, read, update, and delete files.

## Opening a File

```python
file = open('example.txt', 'r')  # Modes: 'r', 'w', 'a', 'b', 'x'
```

## Reading from a File

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

## Writing to a File

```python
with open('example.txt', 'w') as file:
    file.write('Hello, World!')
```

## Appending to a File

```python
with open('example.txt', 'a') as file:
    file.write('\nAppended text.')
```

## Closing a File

Files are automatically closed when using `with`. Otherwise, use:

```python
file.close()
```

## Deleting a File

```python
import os
os.remove('example.txt')
```

## Common File Modes

- `'r'` : Read (default)
- `'w'` : Write (overwrites)
- `'a'` : Append
- `'b'` : Binary mode
- `'x'` : Create (fails if exists)


## Exception Handling in File Operations

It's good practice to handle exceptions when working with files to avoid crashes due to missing files or permission errors.

```python
try:
    with open('example.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("You do not have permission to access this file.")
except Exception as e:
    print(f"An error occurred: {e}")
```


## Common File Handling Errors

- **FileNotFoundError**: Raised when a file or directory is requested but doesn't exist.
- **PermissionError**: Raised when trying to access a file without the required permissions.
- **IsADirectoryError**: Raised when a file operation is requested on a directory.
- **IOError / OSError**: General input/output errors, such as disk full or hardware failure.
- **ValueError**: Raised when an invalid mode is used or the file is closed.
- **UnsupportedOperation**: Raised when an operation (like writing) is not allowed in the current file mode.