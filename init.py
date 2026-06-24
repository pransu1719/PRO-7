from .file_operation import *
from .math import *
 elif choice == "5":
            break

        else:
            print("Invalid Choice")


# ---------------- UUID ----------------

def generate_uuid():
    print("\nGenerated UUID:")
    print(uuid.uuid4())
    print("=" * 30)


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

def explore_module():
    print("\nExplore Module Attributes:")
    module_name = input(
        "Enter module name (math/random/datetime): ")

    if module_name == "math":
        print(dir(math))

    elif module_name == "random":
        print(dir(random))

    elif module_name == "datetime":
        print(dir(datetime))

    else:
        print("Invalid module name")

    print("=" * 30)


# ---------------- MAIN MENU ----------------

def main():
    while True:
        print("\n==============================")
        print("Welcome to Multi-Utility Toolkit")
        print("==============================")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate UUID")
        print("5. File Operations")
        print("6. Explore Module Attributes")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            datetime_menu()

        elif choice == "2":
            math_menu()

        elif choice == "3":
            random_data()     # Fixed here

        elif choice == "4":
            generate_uuid()

        elif choice == "5":
            file_operations()

        elif choice == "6":
            explore_module()

        elif choice == "7":
            print("\nThank you for using the Multi-Utility Toolkit!")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()

