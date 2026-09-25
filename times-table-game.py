import random
import os
import time

def Difficulty():
    try:
        Choice = input("1.Easy (1 - 5 times table) \n2.Medium (1 - 10 times table) \n3.Hard (1 - 15 times table)\nSelect a number for difficulty : ")
        if int(Choice) == 1:
            return 5
        elif int(Choice) == 2:
            return 10
        elif int(Choice) == 3:
            return 15
        else: 
            print("Enter numbers : 1, 2, 3")
    except ValueError:
        print("Enter an integer for the difficulty")

def GenerateQuestion(max_num):
    if (max_num == 15):
        num1 = random.randint(1,max_num-1)
        num2 = random.randint(1,max_num)
        if num2 >= 10:
            num2 +=1
    else:
        num1 = random.randint(1,12)
        num2 = random.randint(1,max_num)
    result = num1*num2
    return num1, num2, result

def Main():
    Score = 0
    max_num = Difficulty()
    while True :
        first_num, second_num, answer = GenerateQuestion(max_num)
        try:
            user_Input = int(input(f"What is {first_num} X {second_num} : "))
        except ValueError: #otherthan
            print("Enter an integer")
            time.sleep(1)
            os.system('cls'
            continue
        if (user_Input != (answer)):
            print(f"incorrect, correct answer is {answer}")
            break
        else:
            Score +=1
            print("The score is ", Score)
            time.sleep(1)
            os.system('cls')

    print("Your final score is, ", Score)   

Main()
