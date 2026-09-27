import random
import os
import time


def leaderboard():
    folder = os.path.dirname(os.path.abspath(__file__))
    leaderboard_file = os.path.join(folder, "LB.txt")
    if os.path.exists(leaderboard_file):
        with open(leaderboard_file, "r") as file:
            scores = [int(line.strip()) for line in file.readlines()]
            scores.sort(reverse=True)
            print("Leaderboard:")
            for i, score in enumerate(scores[:5], start=1):
                print(f"{i}. {score}")

def save_score(score):
    folder = os.path.dirname(os.path.abspath(__file__))
    leaderboard_file = os.path.join(folder, "LB.txt")

    with open(leaderboard_file, "a") as file:
        file.write(f"{score}\n")

def difficulty_level():
    while True:
        try:
            level = int(input("1.Easy (1 - 5 times table) \n2.Medium (1 - 10 times table) \n3.Hard (1 - 15 times table)\nSelect a number for difficulty : "))

            if level == 1:
                print("You have selected Easy level.")
                return 5

            elif level == 2:
                print("You have selected Medium level.")
                return 10

            elif level == 3:
                print("You have selected Hard level.")
                return 15

            else:
                print("Please select a valid difficulty level (1-3).")

        except ValueError:
            print("Please enter a number between 1 and 3.")


def generate_question(max_num):
    num1 = random.randint(1, max_num)

    if max_num == 15:
        num2 = random.randint(1, 14)
        if num2 >=10:
            num2 += 1
    else:
        num2 = random.randint(1, 12)

    result = num1 * num2

    return num1, num2, result


def Main():
    score = 0
    max_num = difficulty_level()

    time.sleep(1)
    os.system('cls')

    while True:
        first_num, second_num, correct_answer = generate_question(max_num)

        try:
            user_input = int(input(f"What is {first_num} x {second_num}? "))

        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_input == correct_answer:
            print("Correct answer")
            score += 1
            time.sleep(1)
            os.system('cls')

        else:
            print("Incorrect answer, the answer is:", correct_answer)
            save_score(score)
            leaderboard()
            break

    print(f"Your final score is: {score}")


Main()
