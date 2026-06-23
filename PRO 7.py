import datetime
import time
import math
import random
import uuid
import string


# ==================== DATETIME MENU =====================

def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            now = datetime.datetime.now()
            print("\nCurrent Date and Time:")
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            print("=" * 30)

        elif choice == "2":
            d1 = input("Enter first date (YYYY-MM-DD): ")
            d2 = input("Enter second date (YYYY-MM-DD): ")

            date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
            date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")

            diff = abs((date2 - date1).days)

            print("Difference:", diff, "days")
            print("=" * 30)

        elif choice == "3":
            now = datetime.datetime.now()

            print(now.strftime("%d/%m/%Y"))
            print(now.strftime("%A, %d %B %Y"))
            print("=" * 30)

        elif choice == "4":
            input("Press ENTER to start stopwatch...")
            start = time.time()

            input("Press ENTER to stop stopwatch...")
            end = time.time()

            print("Elapsed Time:", round(end - start, 2), "seconds")
            print("=" * 30)

        elif choice == "5":
            sec = int(input("Enter countdown seconds: "))

            while sec > 0:
                print(sec)
                time.sleep(1)
                sec -= 1

            print("Time's Up!")
            print("=" * 30)

        elif choice == "6":
            break

        else:
            print("Invalid Choice")


#==================== MATHEMATICAL MENU =====================

def math_menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Circle")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            num = int(input("Enter number: "))
            print("Factorial =", math.factorial(num))

        elif choice == "2":
            p = float(input("Enter principal amount: "))
            r = float(input("Enter rate (%): "))
            t = float(input("Enter time (years): "))

            amount = p * ((1 + r / 100) ** t)

            print("Compound Amount =", round(amount, 2))

        elif choice == "3":
            angle = float(input("Enter angle in degrees: "))

            print("Sin =", round(math.sin(math.radians(angle)), 4))
            print("Cos =", round(math.cos(math.radians(angle)), 4))
            print("Tan =", round(math.tan(math.radians(angle)), 4))

        elif choice == "4":
            radius = float(input("Enter radius: "))

            area = math.pi * radius * radius

            print("Area of Circle =", round(area, 2))

        elif choice == "5":
            break

        else:
            print("Invalid Choice")

        print("=" * 30)


# ================= RANDOM DATA ====================

def random_data():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            a = int(input("Enter minimum value: "))
            b = int(input("Enter maximum value: "))
            print("Random Number:", random.randint(a, b))
            print("=" * 25)

        elif choice == "2":
            n = int(input("Enter list size: "))

            lst = []
            for i in range(n):
                lst.append(random.randint(1, 100))

            print("Random List:", lst)
            print("=" * 25)

        elif choice == "3":
            length = int(input("Enter password length: "))

            chars = string.ascii_letters + string.digits + "!@#$%^&*"
            password = ""

            for i in range(length):
                password += random.choice(chars)

            print("Generated Password:", password)
            print("=" * 25)

        elif choice == "4":
            otp = random.randint(1000, 9999)

            print("Generated OTP:", otp)
            print("=" * 25)

        elif choice == "5":
            break

        else:
            print("Invalid Choice")


# ================= UUID ===================

def generate_uuid():
    print("\nGenerated UUID:")
    print(uuid.uuid4())
    print("=" * 30)


#================FILE OPERATIONS ====================

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


#============== MODULE EXPLORER ==================

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


# =================== MAIN MENU ==========================

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
