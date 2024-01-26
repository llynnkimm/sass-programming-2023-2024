# Chatbot
# Author: Lynn Kim
# Date: 20 September 2023

import random
import time

# Greet the user
print("Hello there! 🤖")
# Pause for 1.5 seconds
time.sleep(1)
print("I'm a crude Chatbot, here to talk to you.")
time.sleep(1)

# Get the user's name and store it in the variable
user_name = input("So... What's your name? ")

time.sleep(1)

# Respond with the user's name in a friendly way
print(f"It's good to meet you, {user_name}.")

time.sleep(1)

# Ask the user what their favourite food is
favourite_food = input("I have a quick question... What is your favourite food? ")

time.sleep(1)

# If their favourite food is sushi, reply with yum.
if favourite_food == "sushi":
    print("Yum! 🍣")
    print("I love sushi!.. I think! 😅")
elif favourite_food == "burgers" or favourite_food == "Burgers":
    print("🍔")
    print("I love burgers!.. I think! 😅")
else:
    # Make a comment about their favourite food but NOT OVERLY REPETITIVE
    # Create a list of possible responses 
    list_of_food_responses = [
        f"Oh, I've never had {favourite_food} before!",
        "Mmmmm. That sounds good!",
        "I heard that that is very good!",
        "That's cool! I want to try that",
        "Oh! that does sound pretty good right about now! 🤠"
    ]

    # Choose one of those responses randomly
    random_food_response = random.choice(list_of_food_responses)

    time.sleep(1)

    # Print out that chosen response
    print(random_food_response)