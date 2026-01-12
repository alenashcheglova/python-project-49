import random

GAME_SCRIPT = 'What number is missing in the progression?'
MIN_START = 1
MAX_START = 100
MIN_STEP = 1
MAX_STEP = 5
MIN_LENGTH = 5
MAX_LENGTH = 10


def get_quest_and_answ():
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)
    length = random.randint(MIN_LENGTH, MAX_LENGTH)

    progression = [start + step * i for i in range(length)]
    hidden_element = random.randint(0, length - 1)
    correct_answ = str(progression[hidden_element])
    progression[hidden_element] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answ