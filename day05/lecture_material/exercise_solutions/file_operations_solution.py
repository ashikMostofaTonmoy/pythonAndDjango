#!/usr/bin/env python3
"""
Exercise 1: Basic File Operations
Create a Python script that:
1. Creates a new text file named "notes.txt"
2. Writes at least three lines of text to it
3. Closes the file
4. Opens the file again and reads the content
5. Prints the content to the console
"""


def create_and_write_file():
    # 1 & 2: Create a new file and write three lines to it
    # Using with statement to ensure the file is properly closed
    with open("notes.txt", "w") as file:
        file.write("This is the first line of my notes file.\n")
        file.write("Here's the second line with more information.\n")
        file.write("And finally, the third line to complete the task.")

    print("File created and written successfully.")


def read_and_print_file():
    # 4: Open the file again and read the content
    try:
        with open("notes.txt", "r") as file:
            content = file.read()

        # 5: Print the content to the console
        print("\nFile content:")
        print("-" * 30)
        print(content)
        print("-" * 30)
    except FileNotFoundError:
        print("Error: The file 'notes.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    create_and_write_file()
    # 3: File is automatically closed due to the 'with' statement
    read_and_print_file()


if __name__ == "__main__":
    main()
