# Olympic Judging
# Author: Kim Lynn
# 7 November 2023

questions = [
    "Judge 1"
    "Judge 2"
    "Judge 3"
    "Judge 4"
    "Judge 5"
]
final_score = 0
for question in questions:
    print(question)
    rating = float(input().strip(",.?!"))
    final_score += rating
average_score = final_score/ len(questions)
print(f"Your Olympic score is: {average_score:.2f}/5")