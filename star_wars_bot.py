# Star Wars Bot
# Author: Lynn Kim
# October 16, 2023

import sys
import time

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.15)

# Create a bot that with a series of yes or no questions that will decide weather your on the light side or dark side

print("Hello I am a Star wars chatbot that will decide if you belong on the light or dark side.")
time.sleep(1)
print("Please answer these yes or no questions honestly.")
time.sleep(1.5)
print("Let's begin.😈")
time.sleep(2)

# Ask the user if they like capes and the colour red
like_red = input("Is red your colour of choice? ")
like_capes = input("Are capes your style? ")
# Give response based on inputs
if like_red.lower() == "yes":
    print("You belong to the dark side of the force.")
elif like_red.lower() == "no":
    if like_capes.lower() == "yes":
        print("Welcome to the darkness.")
    else:
        print("I sense the light within you.")
        time.sleep(2)
        print("Welcome to the light side.")
else:
    delay_print("I sense the light within you.")
    delay_print("Welcome to the light side.")