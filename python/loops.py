# 1. for loop
# Used to iterate over a sequence (like a list, tuple, string, or range).

# ✅ Example: Print numbers from 1 to 5

# for i in range(1, 6):
#     print(i)

# ✅ Example: Loop through a list

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# 2. while loop
# Repeats as long as a condition is true.

# ✅ Example: Print numbers from 1 to 5

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# 3. break and continue statements
# break – Stops the loop completely.

# continue – Skips the current iteration and moves to the next.

# ✅ Example using break

# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)
# # ✅ Example using continue

for i in range(1, 6):
    if i == 3:
        continue
    print(i)