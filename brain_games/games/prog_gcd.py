import random
import math 
GAME_SCRIPT = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 100

def get_quest_and_answ():
    num1 = random.randint(MIN_NUMBER,MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER,MAX_NUMBER)
    question = f'{num1} {num2}'
    correct_answ = str(math.gcd(num1, num2))
    return question, correct_answ
