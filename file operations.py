# ---------------- FILE OPERATIONS ----------------
def create_file():
    filename = input("Enter file name: ")

    with open(filename, "w"):
        pass

    print("File created successfully!")
    print("=" * 30)


def write_file():
    filename = input("Enter file name: ")
    data = input("Enter data to write: ")

    with open(filename, "w") as file:
        file.write(data)

    print("Data written successfully!")
    print("=" * 30)


def read_file():
    filename = input("Enter file name: ")

    try:
        with open(filename, "r") as file:
            print("File Content:")
            print(file.read())

    except FileNotFoundError:
        print("File not found!")

    print("=" * 30)


def append_file():
    filename = input("Enter file name: ")
    data = input("Enter data to append: ")

    with open(filename, "a") as file:
        file.write("\n" + data)

    print("Data appended successfully!")
    print("=" * 30)


def file_operations():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_file()

        elif choice == "2":
            write_file()

        elif choice == "3":
            read_file()

        elif choice == "4":
            append_file()

        elif choice == "5":
            break

        else:
            print("Invalid Choice")


# ---------------- MODULE EXPLORER ----------------


