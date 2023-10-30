# Bubble Tea Popularity Algorithm
# Author: Lynn Kim
# Date: 27 October 2023

# Ask 5 users what their favourite bubble tea place is
# Prints out a summary of the data

# ------ CONSTANTS

NUM_RESPONDENTS = 5

# ------

# Like counters
coco_likes = 0      # Initialize the variable to 0
suntea_likes = 0
chatime_likes = 0
bubqueen_likes = 0

for _ in range(NUM_RESPONDENTS):
    # Ask the user what their favourite place is
    print("What's your favourite bubble tea place?")
    fave_place = input().strip(",.?! ").lower()

    # Tally or counting algo
    if fave_place == "coco":
        coco_likes = coco_likes + 1
    elif fave_place == "suntea":
        suntea_likes += 1       # alternate to above
    elif fave_place == "chatime":
        chatime_likes += 1
    elif fave_place == "bubble queen":
        bubqueen_likes += 1

#  Print out a summary of all the places
#GIve the raw score and the percentage
print(f'CoCo likes: {coco_likes}')
print(f'suntea: {suntea_likes}')
print(f'chatime likes: {chatime_likes}')
print(f'bubqueen likes: {bubqueen_likes}')
# Tally or counting algo
# options: CoCo, Suntea, Chatime, Bubble Queen
# if they choose any of these options, increase the counter
print(f"CoCo percentage: {coco_likes / NUM_RESPONDENTS * 100}%")
print(f"Bubble queen likes: {bubqueen_likes / NUM_RESPONDENTS * 100}%")
print(f"Suntea likes: {suntea_likes / NUM_RESPONDENTS * 100}%")
print(f"Chatime likes: {chatime_likes / NUM_RESPONDENTS * 100}%")