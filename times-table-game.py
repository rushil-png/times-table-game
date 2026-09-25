import random

def GenerateQuestion():
    num1 = random.randint(1,12)
    num2 = random.randint(1,12)
    result = num1*num2
    return num1, num2, result

def Main():
    Score = 0
    while True :
        first_num, second_num, answer = GenerateQuestion()
        try:
            user_Input = int(input(f"What is {first_num} X {second_num} : "))
        except ValueError: #otherthan
            print("Enter an integer")
            continue

        if (user_Input != (answer)):
            print(f"incorrect, correct answer is {answer}")
            break
        else:
            Score +=1
            print("The score is ", Score)

Main()
