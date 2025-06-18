# ==========================================================
# 👋 Welcome to Day 2: Variables, Data Types & Type Casting
# ----------------------------------------------------------
# Today we'll learn:
# ✅ What variables are
# ✅ Common data types: int, float, string, boolean
# ✅ How to convert between data types (type casting)
# Author: Rainsford Kofi Senam
# ==========================================================

# ----------------------------------------
# 🔢 What Are Variables?
# ----------------------------------------
# Think of variables as labeled boxes where you can store data.

# Let's create a few variables:
name = "Rainsford"      # string
age = 25                # integer
height = 5.9            # float
is_student = True       # boolean (True or False)

# Let’s print them
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student status:", is_student)

# ----------------------------------------
# 📚 Python Data Types
# ----------------------------------------

# ➤ Integer (int): Whole numbers
year = 2025
print("This is an integer:", year)

# ➤ Float: Numbers with decimal points
gpa = 3.45
print("This is a float:", gpa)

# ➤ String (str): Text
course = "Python Programming"
print("This is a string:", course)

# ➤ Boolean (bool): True or False values
passed_exam = False
print("Did you pass the exam?", passed_exam)

# You can check the type using type()
print("Type of name is:", type(name))
print("Type of gpa is:", type(gpa))

# ----------------------------------------
# 🔄 Type Casting (Converting Data Types)
# ----------------------------------------

# Sometimes, we need to change data from one type to another.

# ➤ Convert integer to string
age_str = str(age)
print("Age as string:", age_str, "| Type:", type(age_str))

# ➤ Convert float to integer
gpa_whole = int(gpa)  # Note: this removes the decimal part!
print("GPA as whole number:", gpa_whole)

# ➤ Convert string to float (if the string is a number)
num_str = "42.8"
converted_float = float(num_str)
print("Converted string to float:", converted_float)

# ➤ Convert boolean to int
print("True as int:", int(True))   # 1
print("False as int:", int(False)) # 0

# ➤ Convert number to boolean
print("0 as boolean:", bool(0))     # False
print("Any other number as boolean:", bool(5))  # True

# ----------------------------------------
# ⚠️ Be Careful!
# ----------------------------------------
# Trying to convert non-numeric strings to numbers will crash the program!
# Example: float("hello") → ❌ ValueError

# Uncomment the line below to see what happens
# print(float("hello"))  # This will cause an error!

# ----------------------------------------
# 📝 Mini Challenge: Try it Yourself!
# ----------------------------------------

# Uncomment and complete this mini challenge:

# user_age = input("Enter your age: ")  # input is always a string!
# user_age = int(user_age)  # convert it to int
# print(f"In 5 years, you'll be {user_age + 5} years old.")

# ----------------------------------------
# 🎉 Wrapping Up Day 2
# ----------------------------------------

print("🎉 Great job! You now know how to use variables, data types, and type casting in Python.")
print("On Day 3, we’ll dive into simple calculations and decision making with if-else!")

# 🏁 END OF DAY 2
