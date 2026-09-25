import random
import os
import time


def generate_question():
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    result = num1 * num2
    return num1, num2, result

def Main():
    score = 0

    while True:
        first_num, second_num, correct_answer = generate_question()
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
            print("Incorrect answer, the answer is: ", correct_answer)
            break

    print(f"Your final score is: {score}")

Main()
