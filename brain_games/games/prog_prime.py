import random

GAME_SCRIPT = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_quest_and_answ():
    num = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = str(num)
    correct_answ = 'yes' if is_prime(num) else 'no'
    return question, correct_answ