# ===================================================
# 👋 Welcome to Day 1: Getting Started with Python
# ---------------------------------------------------
# In this lesson, we’ll cover:
# - What Python is
# - Installing it
# - Writing your first lines of code
# - Basic syntax
# - Using the print() function
# - Writing comments
# Author: Rainsford Kofi Senam
# ===================================================

# ----------------------------------------
# 🐍 What is Python?
# ----------------------------------------
# Python is a programming language that’s clean, beginner-friendly,
# and used in lots of fields — from websites to AI.
# You don't need to know everything now. Let's start small!

# ----------------------------------------
# 🛠️ Installation (Skip if already done)
# ----------------------------------------
# 👉 Go to https://python.org and download Python for your OS.
# ✅ Don’t forget to check "Add Python to PATH" during install.
# Open a terminal and type: python --version
# If it works, you’re good to go!

# ----------------------------------------
# 👋 Hello, Python!
# ----------------------------------------

print("Hello, World!")  # Your very first line of Python!
print("Welcome to Day 1 of your Python journey.")
print("Let's take this one step at a time 😊")

# ----------------------------------------
# 🧠 Variables and Print
# ----------------------------------------

name = "Rainsford"
age = 25

print("My name is", name)
print("I am", age, "years old.")

# Let's make it fancier using f-strings
print(f"{name} is learning Python at the age of {age}!")

# Special characters
print("This is the first line.\nAnd this is the second line.")
print("She said, \"Python is fun!\" and I totally agree.")

# ----------------------------------------
# 💬 Comments in Python
# ----------------------------------------

# This is a comment. Python skips these lines.
# Use them to explain your code, or to leave notes for yourself.

"""
Triple quotes like these are used for multi-line comments or docstrings.
They’re handy for writing explanations that span multiple lines.
"""

# ----------------------------------------
# 🧩 Python Syntax Basics
# ----------------------------------------

# Python doesn’t use curly braces like other languages.
# It uses indentation (tabs or 4 spaces) to define code blocks.

language = "Python"
version = 3.11
is_fun = True

print("Language:", language)
print("Version:", version)
print("Is Python fun?", is_fun)

# Let’s try a simple if-statement
if age >= 18:
    print("You’re an adult and ready to code!")

# ----------------------------------------
# 📝 Mini Exercise: Your Turn!
# ----------------------------------------

# Try asking the user for their name and favorite color
# Uncomment the lines below to test it!

# your_name = input("What's your name? ")
# favorite_color = input("What's your favorite color? ")
# print(f"Nice to meet you, {your_name}! {favorite_color} is a great color!")

# ----------------------------------------
# 💡 Bonus: Multi-line Print
# ----------------------------------------

print("""
"Programming isn't about what you know;
it's about what you can figure out." – Chris Pine
""")

# ----------------------------------------
# 🎉 Wrapping Up Day 1
# ----------------------------------------

print("Awesome! 🎉 You've completed Day 1 of Python.")
print("Take a break, or try writing your own mini intro script!")

# 🏁 END OF DAY 1
