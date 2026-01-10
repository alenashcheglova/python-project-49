import random
import math 
GAME_SCRIPT = 'Find the greatest common divisor of given numbers.'

def get_quest_and_answ():
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    question = f'{num1} {num2}'
    correct_answ = str(math.gcd(num1, num2))
    return question, correct_answ
