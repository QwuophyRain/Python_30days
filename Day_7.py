# ============================================================
# 👋 Welcome to Day 7: While Loops, Break, and Continue
# ------------------------------------------------------------
# Today you’ll learn:
# ✅ How to use while loops (loop until something is false)
# ✅ How to stop a loop early using break
# ✅ How to skip part of a loop using continue
# ✅ Hands-on examples to practice control flow
# Author: Rainsford Kofi Senam
# ============================================================

# ----------------------------------------
# 🔁 1. What is a While Loop?
# ----------------------------------------
# A while loop keeps running as long as a condition is True.

count = 1

while count <= 5:
    print("Counting:", count)
    count += 1

# If you're not careful, a while loop can run forever!
# Example (DON'T RUN THIS!):
# while True:
#     print("This never ends...")

# ----------------------------------------
# ⛔ 2. The break Statement
# ----------------------------------------
# `break` stops the loop immediately — like hitting "Exit" early.

print("Break example:")
i = 0
while i < 10:
    if i == 5:
        break  # Stop loop when i hits 5
    print("i =", i)
    i += 1

# ----------------------------------------
# 🔁 3. The continue Statement
# ----------------------------------------
# `continue` skips the rest of the current loop and goes to the next one.

print("Continue example (skip 3):")
j = 0
while j < 6:
    j += 1
    if j == 3:
        continue  # Skip number 3
    print("j =", j)

# ----------------------------------------
# 🧠 4. Real-World Example: Login Attempts
# ----------------------------------------

correct_password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Enter password: ")
    if user_input == correct_password:
        print("Access granted ✅")
        break
    else:
        print("Wrong password ❌")
        attempts += 1

if attempts == max_attempts:
    print("Too many attempts. Try again later.")

# ----------------------------------------
# 🛠️ 5. Try It Yourself: Mini Projects
# ----------------------------------------

# 💡 Project 1: Guess the Number Game
# secret = 7
# guess = 0
# while guess != secret:
#     guess = int(input("Guess a number (1-10): "))
#     if guess == secret:
#         print("🎯 You got it!")
#     else:
#         print("Try again!")

# 💡 Project 2: Print Even Numbers up to 20 (using continue)
# number = 0
# while number <= 20:
#     number += 1
#     if number % 2 != 0:
#         continue  # Skip odd numbers
#     print("Even number:", number)

# 💡 Project 3: Countdown with Break
# timer = 10
# while timer > 0:
#     print("Countdown:", timer)
#     if timer == 3:
#         print("⏹ Countdown stopped early!")
#         break
#     timer -= 1

# ----------------------------------------
# ⚠️ Common Mistakes to Watch
# ----------------------------------------

# ❌ Forgetting to update the condition variable (causes infinite loop)
# ❌ Using = instead of == in conditions
# ❌ Misplacing break or continue (can cause bugs)

# ----------------------------------------
# 🎉 Wrapping Up Day 7
# ----------------------------------------

print("🎉 Well done! You've mastered while loops and how to control them.")
print("Coming up next: Day 8 — Lists in Python (storing multiple values).")

# 🏁 END OF DAY 7
