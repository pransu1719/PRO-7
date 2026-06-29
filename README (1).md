# 🧰 Multi-Utility Toolkit (Python CLI)

A menu-driven, command-line "Swiss Army knife" built in Python. It bundles
together several handy everyday tools — date/time helpers, math operations,
random data generators, UUID creation, basic file operations, and a built-in
module explorer — all from one simple text menu.

## ✨ Features

| # | Menu Option | What it does |
|---|---|---|
| 1 | **Datetime and Time Operations** | Show current date/time, find the difference between two dates, format dates, run a stopwatch, run a countdown timer |
| 2 | **Mathematical Operations** | Factorial, compound interest, trigonometric values (sin/cos/tan), area of a circle |
| 3 | **Random Data Generation** | Random number, random list, random password, random OTP |
| 4 | **Generate UUID** | Generate a unique UUID4 identifier |
| 5 | **File Operations** | Create, write, read, and append to text files |
| 6 | **Explore Module Attributes** | List all available functions/attributes of `math`, `random`, or `datetime` |
| 7 | **Exit** | Closes the toolkit |

Every sub-menu loops back to itself until you choose to go back, so you can
run multiple operations without restarting the program.

## 📂 Project Structure

```
multi-utility-toolkit/
├── pro_7.py             # Main program — run this file
├── file_operations.py   # Standalone copy of the File Operations module
├── math_utils.py        # Standalone math helper functions
├── init.py              # Package init file (currently empty)
├── screenshots/         # Sample run screenshots (see below)
└── README.md
```

> **Note:** `pro_7.py` is fully self-contained — it already includes the file
> operations and math logic inline, so `file_operations.py` and
> `math_utils.py` are kept here as separate reference modules.

## ▶️ How to Run

Requires Python 3.7+ (uses only the standard library — no extra installs
needed).

```bash
python pro_7.py
```

Then just follow the on-screen menu and type the number of the option you
want.

## 🖼️ Sample Output

**Main Menu**

![Main Menu](screenshots/111.png)

**Datetime Operations — current time & date difference**

![Datetime Operations](screenshots/112.png)

**Mathematical Operations — factorial**

![Math Menu - Factorial](screenshots/113.png)

**Mathematical Operations — compound interest**

![Math Menu - Compound Interest](screenshots/114.png)

**Random Data Generation — password**

![Random Data - Password](screenshots/115.png)

**Random Data Generation — back to main menu**

![Random Data Menu](screenshots/116.png)

**UUID Generation**

![UUID Generation](screenshots/117.png)

**File Operations — create & write**

![File Operations](screenshots/118.png)

**File Operations — read content**

![File Read](screenshots/119.png)

**Explore Module Attributes — math module**

![Explore Module](screenshots/120.png)

**Exit**

![Exit](screenshots/120.png)

## ⚠️ Known Issue

In `math_utils.py`, the `factorial()` function calls `mathfactorial(n)`
instead of `math.factorial(n)` — this is a typo and will raise a
`NameError` if used. The main program (`pro_7.py`) is unaffected since it
calls `math.factorial()` directly in `math_menu()`.

```python
# math_utils.py — current (buggy)
def factorial(n):
    return mathfactorial(n)   # ❌ should be math.factorial(n)
```

## 🚀 Possible Improvements

- Fix the `factorial()` typo in `math_utils.py`
- Add input validation (currently invalid input like text instead of numbers
  will crash the program)
- Add unit tests
- Split into a proper Python package using `init.py`

## 📜 License

Free to use and modify for learning purposes.
