import prompt

from brain_games.constants import ROUNDS


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_SCRIPT)

    for _ in range(ROUNDS):
        question, correct_answ = game.get_quest_and_answ()
        print(f'Question: {question}')
        user_answ = prompt.string('Your answer: ')

        if user_answ == correct_answ:
            print('Correct!')
        else:
            print(f"'{user_answ}' is wrong answer ;(. "
                  f"Correct answer is '{correct_answ}'.")
            print(f"Let's try again, {name}!")
            return
        
    print(f'Congratulations, {name}!')