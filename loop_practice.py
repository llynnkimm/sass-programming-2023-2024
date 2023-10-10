# Loop Practice
# Author: Lynn Kim
# Date: 10 October 2023

# Create a list of groceries
groceries = ["hot wheels", "lego", "ice cream"]

# Do something for each thing in the list
# Print it out in a pretty way
# e.g.
#   * hot wheels
#     ---
#   * lego
#     ---
#     etc.

# print(f"* {groceries[0]}")
# print(f" ---")
# print(f"* {groceries[1]}")
# print(f" ---")
# print(f"* {groceries[2]}")
# print(f" ---")

for item in groceries :
    print(f"* {item}")
    print(" ---")

# Using the above method, create the thing below:
# *
# **
# ***
# ****
# *****
# ******

# Create a list of asterisks
asterisks = ["*", "**", "***", "****", "*****", "******"]

for item in asterisks :
    print(f"{item}")

# Problem:
# Create a New Year's Countdown that's automated
# Requirements:
#   - starts at 10
#   - counts down every second printing the second that it's at
#   - instead of reaching zero, it prints out "Happy New Year!"
# Example Output:
# 10
# 9 
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# Happy New Year!

# Create a New Years Countdown
Countdown = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "Happy New Year!"]

import time

for item in Countdown :
    print(f"{item}")
    time.sleep(1)