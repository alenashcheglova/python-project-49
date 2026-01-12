import random

GAME_SCRIPT = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_quest_and_answ():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(['+', '-', '*'])
    match operator:
        case '+':
            correct_answ = num1 + num2
        case '-':
            correct_answ = num1 - num2
        case '*':
            correct_answ = num1 * num2
    question = f"{num1} {operator} {num2}"
    return question, str(correct_answ)