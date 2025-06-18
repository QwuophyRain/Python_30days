# ===========================================================
# 👋 Welcome to Day 4: User Input & Type Conversion
# -----------------------------------------------------------
# Today you’ll learn how to:
# ✅ Accept input from a user
# ✅ Convert that input to numbers or other types
# ✅ Combine input with print statements and variables
# ✅ Practice with fun mini-projects
# Author: Rainsford Kofi Senam
# ===========================================================

# ----------------------------------------
# 🧑‍💻 1. Getting Input from the User
# ----------------------------------------

# Let's ask the user for their name
name = input("What's your name? ")
print("Hello", name + "! Nice to meet you 😊")

# Input always returns a STRING
# Even if the user types a number, it's still a string

# Example:
age = input("How old are you? ")
print("You said your age is:", age)
print("Type of age variable is:", type(age))  # This will show <class 'str'>

# ----------------------------------------
# 🔄 2. Type Conversion (Casting)
# ----------------------------------------

# To do math, we need to convert the input into a number (int or float)

# Let's ask the user for two numbers
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Convert to integers
num1 = int(num1)
num2 = int(num2)

# Now we can add them
print("The sum is:", num1 + num2)

# Let's try floats
num3 = float(input("Enter a decimal number: "))
num4 = float(input("Enter another decimal number: "))
print("The product is:", num3 * num4)

# ----------------------------------------
# 🔍 3. Examples of Conversions
# ----------------------------------------

# str() → converts to string
# int() → converts to integer
# float() → converts to decimal
# bool() → converts to True/False

print("int('42') =", int("42"))         # 42
print("float('3.14') =", float("3.14")) # 3.14
print("str(99) =", str(99))             # "99"
print("bool(0) =", bool(0))             # False
print("bool(1) =", bool(1))             # True

# ----------------------------------------
# 🚨 Watch Out!
# ----------------------------------------

# You can't convert a word like "hello" into a number
# This will crash the program:
# int("hello") ❌

# Uncomment to test the error:
# print(int("hello"))

# ----------------------------------------
# 🛠️ 4. Try It Yourself: Mini Projects
# ----------------------------------------

# 💡 Project 1: Age Calculator
# Ask the user their birth year and calculate their age

# Uncomment to run:
# birth_year = int(input("Enter your birth year: "))
# current_year = 2025
# age = current_year - birth_year
# print("You are", age, "years old.")

# 💡 Project 2: Area of a Rectangle
# Ask user for length and width, then calculate area

# Uncomment to run:
# length = float(input("Enter the length (m): "))
# width = float(input("Enter the width (m): "))
# area = length * width
# print("Area of the rectangle is:", area, "square meters")

# 💡 Project 3: Tip Calculator
# Ask for bill amount and tip %, then calculate total

# Uncomment to run:
# bill = float(input("Enter your bill amount: GHS "))
# tip_percent = float(input("Enter tip percentage (e.g. 10 for 10%): "))
# tip_amount = (tip_percent / 100) * bill
# total = bill + tip_amount
# print("You should tip: GHS", tip_amount)
# print("Total to pay: GHS", total)

# ----------------------------------------
# 💡 Bonus: Chaining Input and Conversion
# ----------------------------------------

# You can do this in one line:
# score = int(input("Enter your exam score: "))
# print("Double your score is:", score * 2)

# ----------------------------------------
# 🎉 Wrapping Up Day 4
# ----------------------------------------

print("🎉 Great work today! You've just learned how to get user input and convert it for calculations.")
print("Tomorrow, we’ll make decisions in code using if-else — it’s going to be fun!")

# 🏁 END OF DAY 4
