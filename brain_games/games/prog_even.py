import random 
GAME_SCRIPT = 'Answer "yes" if the number is even, otherwise answer "no".'

def is_even(num):
    return num % 2 == 0

def get_quest_and_answ():
    num = random.randint(1, 100)
    correct_answ = 'yes' if is_even(num) else 'no'
    return str(num), correct_answ