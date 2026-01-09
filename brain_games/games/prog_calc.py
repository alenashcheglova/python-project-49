import random
GAME_SCRIPT = 'What is the result of the expression?'

def get_quest_and_answ():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
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