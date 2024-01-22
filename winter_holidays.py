# Winter Holidays 
# Author: Lynn Kim
# 8 January 2024

# Requirements:
# - create a function called winter holiday()
#   - takes one parameter - string 
#   - returns a summary of an event from your holidays 

# Please do not use ChatGPT or any LLM

import random

def winter_holiday(good_or_bad: str) -> str:
    """Give a summary of our winter holidays 2023/24
    
    Params:
        good_or_bad - string that indicates whether the event
            is good or bad
            
    Returns:
        an event that happened to you during the holidays
        the event is selected part"""

"""Secret Santa is happening.
OK. What is your gift wish? 🎮🎮"""

def main() -> None:
    # Runs all the things we want to test in our .py file
    winter_holiday("good")
    # "I got a Lego set for the first time in a long time."
    # "I went to Richmond Center to walk around aimlessly."
    winter_holiday("bad")
    # "I hoped to snowboard during the holidays and there was only rain."
    # "I asked for ________ for christmas, instead I got a random smart watch."


# If we're running THIS FILE using Python
    if __name__ == "__main__":
        main()








# Winter Holidays 
# Author: Lynn Kim
# 8 January 2024
        
# Requirements:
# - create a function called winter holiday()
#   - takes one parameter - string 
#   - returns a summary of an event from your holidays 

# Please do not use ChatGPT or any LLM

import random

def winter_holiday(good_or_bad: str) -> str:
    """Give a summary of our winter holidays 2023/24
    
    Params:
        good_or_bad - string that indicates whether the event
            is good or bad
            
    Returns:
        an event that happened to you during the holidays
        the event is selected part"""

    """Secret Santa is happening.
    OK. What is your gift wish? 🎮🎮"""

    # Create a list of good and bad events
    good_events = [
        "I watched alot of movies",
        "It was my birthday",
        "Ate alot of good food",
        "Slept alot"
        ]
    bad_events = [
        "I worked alot",
        "Spent alot of money",
        "Didn't get anything from Santa"
        ]

    # If the event is good, return a good event
    # Todo: Return a randomly chosen good event
    if good_or_bad.strip().lower() == "good":
        return random.choice(good_events)
    if good_or_bad.strip().lower() == "bad":
        return random.choice(bad_events)

def main() -> None:
    # Runs all the things we want to test in our .py file
    print(winter_holiday("good"))
    # "I got a Lego set for the first time in a long time"
    # "I went to Richmond Centre to walk around aimlessly."
    print(winter_holiday("bad"))
    # "I hoped to snowboard during the holiday and there was only rain."
    #"I asked for _____ for Christmas, instead I got a random smart watch."

# If we're running THIS FILE using Python
    if __name__ == "__main__":
        main()