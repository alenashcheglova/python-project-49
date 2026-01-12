import random

GAME_SCRIPT = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_even(num):
    return num % 2 == 0


def get_quest_and_answ():
    num = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answ = 'yes' if is_even(num) else 'no'
    return str(num), correct_answ