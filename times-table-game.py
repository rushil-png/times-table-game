import random

def generate_question():
    num1 = random.randint(1,12)
    num2 = random.randint(1,12)
    result = num1 * num2
    return num1, num2, result

def Main():
    score = 0
    while True:
        first_num, second_num, correct_answer = generate_question()
        print(f"What is {first_num} x {second_num}?")
        user_input = ("Enter your answer:")
