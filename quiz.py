#HENROLD

QUESTIONFILE = "questions" # file to get questions from

import csv

print("Welcome to my quiz!\n")

with open(f"{QUESTIONFILE}.csv", newline="") as f: # Extract questions from file
    reader = csv.reader(f)
    questions = list(reader)

questioncount = 0
score = 0

while True:
    try:
        print(f"{questions[questioncount][0]}?\n")
    except: # this error will occur if there are no more questions
        break

    answer = input().lower()
    if answer == questions[questioncount][1]:
        print("\nCorrect\n")
        score += 1
    else:
        print("\nIncorrect")
        print(f"The answer was: {questions[questioncount][1]}\n")

    questioncount += 1

print(f"Well Done!\nScore: {score}")
