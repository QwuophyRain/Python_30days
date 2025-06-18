# ============================================================
# 👋 Welcome to Day 3: Operators in Python
# ------------------------------------------------------------
# Today we’ll learn:
# ✅ Arithmetic operators (+, -, *, /, etc.)
# ✅ Comparison operators (==, !=, >, <, etc.)
# ✅ Logical operators (and, or, not)
# ✅ Assignment operators (=, +=, -=, etc.)
# Author: Rainsford Kofi Senam
# ============================================================

# ----------------------------------------
# ➕ 1. Arithmetic Operators
# ----------------------------------------
# These are used for basic math operations.

a = 10
b = 3

print("a =", a)
print("b =", b)

print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.333...
print("Floor Division:", a // b) # 3 (removes decimal part)
print("Modulus (Remainder):", a % b)  # 1
print("Exponent:", a ** b)       # 10^3 = 1000

# ----------------------------------------
# 🧮 2. Comparison Operators
# ----------------------------------------
# These return True or False.

print("Is a equal to b?", a == b)      # False
print("Is a not equal to b?", a != b)  # True
print("Is a greater than b?", a > b)   # True
print("Is a less than b?", a < b)      # False
print("Is a >= b?", a >= b)            # True
print("Is a <= b?", a <= b)            # False

# ----------------------------------------
# 🔗 3. Logical Operators
# ----------------------------------------
# Used to combine multiple conditions

x = 5
y = 8

# and: Both must be True
print("x > 3 and y > 5:", x > 3 and y > 5)  # True

# or: At least one must be True
print("x > 10 or y > 5:", x > 10 or y > 5)  # True

# not: Flips the result
print("not(x > 3):", not(x > 3))  # False

# Let's see a combined example
is_adult = True
has_ticket = False

print("Can enter event?", is_adult and has_ticket)  # False

# ----------------------------------------
# 📝 4. Assignment Operators
# ----------------------------------------
# These assign and update values in variables

score = 10
print("Initial score:", score)

score += 5   # Same as score = score + 5
print("After += 5:", score)

score -= 3   # Same as score = score - 3
print("After -= 3:", score)

score *= 2   # score = score * 2
print("After *= 2:", score)

score /= 4   # score = score / 4
print("After /= 4:", score)

# You can also use %=, //=, **= for other operations

# ----------------------------------------
# ⚠️ Common Mistakes
# ----------------------------------------

# Beware of = vs ==
# = is for assignment, == is for comparison

# Example:
# wrong: if x = 5   ❌
# correct: if x == 5 ✅

# ----------------------------------------
# 🎯 Mini Challenge
# ----------------------------------------

# Try solving this:
# You have $100. You spend $25 on food, $30 on transport.
# Use variables and operators to calculate how much is left.

# Uncomment and try:
# budget = 100
# food = 25
# transport = 30
# budget -= food + transport
# print("Remaining money:", budget)

# ----------------------------------------
# 🎉 Wrapping Up Day 3
# ----------------------------------------

print("🎉 Well done! You’ve just mastered Python operators.")
print("Next up: Making decisions using if-else and building interactive logic!")

# 🏁 END OF DAY 3
