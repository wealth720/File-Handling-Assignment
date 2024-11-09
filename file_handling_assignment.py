# File: file_handling_assignment.py

def create_file():
    try:
        # File Creation: Create and write to the file
        with open("my_file.txt", "w") as file:
            file.write("Line 1: Hello, World!\n")
            file.write("Line 2: 12345\n")
            file.write("Line 3: Python is awesome!\n")
        print("File created and written successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

def read_file():
    try:
        # File Reading and Display: Read and print the file contents
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("File contents:")
            print(content)
    except FileNotFoundError:
        print("The file was not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")

def append_to_file():
    try:
        # File Appending: Open the file in append mode and write more lines
        with open("my_file.txt", "a") as file:
            file.write("Line 4: Adding more content.\n")
            file.write("Line 5: 67890\n")
            file.write("Line 6: File handling in Python.\n")
        print("Additional lines appended successfully.")
    except FileNotFoundError:
        print("The file was not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print(f"An unexpected error occurred while appending to the file: {e}")

# Error Handling demonstration
try:
    create_file()
    read_file()
    append_to_file()
    read_file()  # Read again to display the updated content
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File handling operations completed.")
