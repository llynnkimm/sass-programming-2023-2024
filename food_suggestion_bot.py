# Food Suggestion Bot
# Author: Lynn Kim
# Ocotber 16 2023

# A bot that asks the user what their favourite food is. Based on that food, it will classify the type/genre/cuisine of the food,
# then give a restaurant suggestion.

import random
import time

# Introduce the bot to the user
# Ask the user what their favourite food is
print("Hello, I am here to suggest you a restaurant")
time.sleep(1)
fave_food = input("To help me suggest a restarant, tell me what your favourite food is")
time.sleep(1)

# Italian Cuisine
italian_food = ["pasta", "pizza", "canneloni", "tiramisu"]
filipino_food = ["filipino food", "lumpia", "pancit", "chicken adobo", "adobo", "sisig", "sinigang", "lechon", "kare-kare", "kare kare"]

# If they answer with Italian food, suggest an Italian restaurant
# Suggest another cuisine
# If they answer with Filipino food, suggest a Filipino restaurant
if fave_food.lower().strip("!.,? ") in italian_food:
    print("I see that you might like Italian food")
    time.sleep(1)
    print("I suggest Broli Kitchen.")
    time.sleep(1)
    print("Here's their address.")
    print("186-8180 No 2 Road, Richmond, BC")
elif fave_food.lower().strip("!.,? ") in filipino_food:
    print("I see that you might like Mr. Ubial's people's food")
    time.sleep(1)
    print("I suggest Mr. Ubial's parent's house")
    time.sleep(1)
    print("I heard his mom's a great cook")
    time.sleep(1)
    print("Or I recommend Little Ongpin.")
    time.sleep(1)
    print("Here's there address:")
    print("4093 No 5 Rd, Richmond, BC V6X 2T9")
else:
    print("Sorry, I'm not sure what kind of food that is.")
    time.sleep(1)
    print("Unfortuately I cannot provide a suggestion.")