# =============================================================
# 👋 Welcome to Day 6: Loops in Python (for + range)
# -------------------------------------------------------------
# Today you’ll learn:
# ✅ What loops are and why we need them
# ✅ How to use 'for' loops to repeat code
# ✅ The powerful range() function
# ✅ Practice with fun examples and challenges
# Author: Rainsford Kofi Senam
# =============================================================

# ----------------------------------------
# 🔁 1. What is a Loop?
# ----------------------------------------
# A loop lets your code repeat itself, which saves time and avoids repetition.

# Instead of writing this:
print("Hello!")
print("Hello!")
print("Hello!")

# You can loop it!
for i in range(3):
    print("Hello! (from loop)")

# ----------------------------------------
# 🔹 2. The for Loop
# ----------------------------------------
# A for loop repeats a block of code a certain number of times

for i in range(5):
    print("Looping...", i)

# This loop:
# - starts at 0 by default
# - stops at 4 (one less than 5)

# ----------------------------------------
# 🔢 3. The range() Function
# ----------------------------------------
# range(start, stop, step)

print("Count from 1 to 5:")
for number in range(1, 6):
    print(number)

print("Count by twos:")
for number in range(0, 11, 2):
    print(number)

print("Countdown from 5 to 1:")
for number in range(5, 0, -1):
    print(number)

# ----------------------------------------
# 🧠 4. Using Loops with Strings or Lists
# ----------------------------------------

word = "Python"
for letter in word:
    print("Letter:", letter)

# Or loop through a list:
colors = ["red", "green", "blue"]
for color in colors:
    print("I like", color)

# ----------------------------------------
# 🛠️ 5. Try It Yourself: Mini Projects
# ----------------------------------------

# 💡 Project 1: Print Multiplication Table (e.g., 3 times table)
# for i in range(1, 11):
#     print(f"3 x {i} = {3 * i}")

# 💡 Project 2: Sum of Numbers from 1 to 100
# total = 0
# for i in range(1, 101):
#     total += i
# print("Sum from 1 to 100 is:", total)

# 💡 Project 3: Repeated User Greetings
# name = input("What's your name? ")
# times = int(input("How many times should I greet you? "))
# for i in range(times):
#     print(f"Hello, {name}! ({i + 1})")

# ----------------------------------------
# ⚠️ Tips and Notes
# ----------------------------------------

# range(5) → 0, 1, 2, 3, 4 (not 5)
# You can use any variable name, not just "i" or "number"
# You can also nest loops (loops inside loops), but we’ll explore that later!

# ----------------------------------------
# 🎉 Wrapping Up Day 6
# ----------------------------------------

print("🎉 You’ve just taught Python how to repeat itself!")
print("Next up: Day 7 — while loops and loop control (break & continue).")

# 🏁 END OF DAY 6
