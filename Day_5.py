# ============================================================
# 👋 Welcome to Day 5: Control Flow (if, elif, else)
# ------------------------------------------------------------
# Today you’ll learn:
# ✅ How to make your code "think" and "choose"
# ✅ Use if, elif, and else to control what your program does
# ✅ Write programs that respond to different inputs
# Author: Rainsford Kofi Senam
# ============================================================

# ----------------------------------------
# 🧠 1. What is Control Flow?
# ----------------------------------------
# Control flow allows your program to *make decisions* based on conditions.
# Like: "If it’s raining, bring an umbrella. Else, go without one."

# ----------------------------------------
# 🔹 2. The if Statement
# ----------------------------------------

temperature = 30

if temperature > 25:
    print("It's hot outside! ☀️")
    
# The condition inside `if` must return True or False

# ----------------------------------------
# 🔹 3. if...else Statement
# ----------------------------------------

is_raining = True

if is_raining:
    print("Take an umbrella ☔")
else:
    print("Enjoy the sunshine 😎")

# ----------------------------------------
# 🔹 4. if...elif...else (Multiple Conditions)
# ----------------------------------------

score = 85

if score >= 90:
    print("Grade: A 🎉")
elif score >= 80:
    print("Grade: B 🙂")
elif score >= 70:
    print("Grade: C 😐")
else:
    print("Grade: F 😢 Keep trying!")

# ----------------------------------------
# 🔍 5. Comparison Operators Recap
# ----------------------------------------
# ==   Equal to
# !=   Not equal to
# >    Greater than
# <    Less than
# >=   Greater or equal
# <=   Less or equal

# ----------------------------------------
# 🔄 6. Combining Conditions with Logical Operators
# ----------------------------------------

age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Access granted 🎟️")
else:
    print("Sorry, you can't enter.")

# Try "or" and "not" too!
# if age < 18 or not has_ticket:
#     print("Entry denied.")

# ----------------------------------------
# 🛠️ 7. Try It Yourself: Mini Projects
# ----------------------------------------

# 💡 Project 1: Even or Odd Checker
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("It's even.")
# else:
#     print("It's odd.")

# 💡 Project 2: Simple Login System
# username = input("Enter username: ")
# password = input("Enter password: ")

# if username == "admin" and password == "1234":
#     print("Login successful ✅")
# else:
#     print("Invalid login ❌")

# 💡 Project 3: Number Guessing
# secret = 7
# guess = int(input("Guess a number between 1 and 10: "))
# if guess == secret:
#     print("🎯 You guessed right!")
# elif guess < secret:
#     print("Too low ⬇️")
# else:
#     print("Too high ⬆️")

# ----------------------------------------
# 💡 Bonus: Nesting Conditions
# ----------------------------------------

# Example of a nested if
# age = int(input("Enter your age: "))
# if age >= 18:
#     has_id = input("Do you have an ID? (yes/no): ")
#     if has_id == "yes":
#         print("Welcome in! 🎉")
#     else:
#         print("Sorry, you need ID.")
# else:
#     print("You're too young to enter.")

# ----------------------------------------
# 🎉 Wrapping Up Day 5
# ----------------------------------------

print("🎉 You’ve just unlocked the power of logic and decisions in Python!")
print("Next up: Day 6 — Loops! We'll teach Python how to repeat things smartly.")

# 🏁 END OF DAY 5
