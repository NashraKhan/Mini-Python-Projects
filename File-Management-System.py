# ======================================================
# Simple File Handling Program in Python
# ======================================================
# This program demonstrates the basic file handling operations
# such as creating, writing, reading, copying, counting, and deleting files.
# It uses Python’s built-in open(), read(), write(), seek(), tell(), and os.remove() functions.

import os  # Importing 'os' module for performing delete operation on files

while True:
    # Displaying menu options to the user
    print("\n===== FILE HANDLING MENU =====")
    print("1. Create a new file")
    print("2. Write to an existing file")
    print("3. Overwrite existing content in a file")
    print("4. Read the contents of a file")
    print("5. Find and change file cursor position")
    print("6. Count number of characters, words & lines")
    print("7. Copy contents to another file")
    print("8. Delete a file")
    print("0. Exit")

    # Taking user input for the operation
    choice = int(input("\nEnter your choice (0-8): "))

    # ------------------------------------------------------
    # 1. Create a new file
    # ------------------------------------------------------
    if choice == 1:
        fname = input("Enter file name: ")
        f = open(fname, "x")
        print("File created successfully!")
        f.close()

    # ------------------------------------------------------
    # 2. Write to an existing file (Append mode)
    # ------------------------------------------------------
    elif choice == 2:
        fname = input("Enter file name: ")
        f = open(fname, "a")
        data = input("Enter text to write to the file: ")
        f.write(data + "\n")
        print("Data written successfully!")
        f.close()

    # ------------------------------------------------------
    # 3. Overwrite the existing content in the file
    # ------------------------------------------------------
    elif choice == 3:
        fname = input("Enter file name: ")
        f = open(fname, "w")
        data = input("Enter new content: ")
        f.write(data + "\n")
        print("File content overwritten!")
        f.close()

    # ------------------------------------------------------
    # 4. Read the contents of a file
    # ------------------------------------------------------
    elif choice == 4:
        fname = input("Enter file name: ")
        f = open(fname, "r")
        print("\nFile contents:\n")
        print(f.read())
        f.close()

    # ------------------------------------------------------
    # 5. Find and change the file cursor position
    # ------------------------------------------------------
    elif choice == 5:
        fname = input("Enter file name: ")
        f = open(fname, "r")
        print("Current cursor position:", f.tell())
        pos = int(input("Enter new cursor position (byte offset): "))
        f.seek(pos)
        print("Cursor moved to:", f.tell())
        print("Data from new position:\n", f.read())
        f.close()

    # ------------------------------------------------------
    # 6. Count number of characters, words, and lines
    # ------------------------------------------------------
    elif choice == 6:
        fname = input("Enter file name: ")
        f = open(fname, "r")
        data = f.read()
        lines = data.split('\n')
        words = data.split()
        print("No. of characters:", len(data))
        print("No. of words:", len(words))
        print("No. of lines:", len(lines))
        f.close()

    # ------------------------------------------------------
    # 7. Copy contents from one file to another
    # ------------------------------------------------------
    elif choice == 7:
        src = input("Enter source file name: ")
        dst = input("Enter destination file name: ")
        f1 = open(src, "r")
        f2 = open(dst, "w")
        f2.write(f1.read())
        print("File copied successfully!")
        f1.close()
        f2.close()

    # ------------------------------------------------------
    # 8. Delete a file
    # ------------------------------------------------------
    elif choice == 8:
        fname = input("Enter file name to delete: ")
        os.remove(fname)
        print("File deleted successfully!")

    # ------------------------------------------------------
    # 0. Exit the program
    # ------------------------------------------------------
    elif choice == 0:
        print("Exiting the program. Goodbye!")
        break

    # ------------------------------------------------------
    # Invalid choice
    # ------------------------------------------------------
    else:
        print("Invalid choice! Please try again.")
