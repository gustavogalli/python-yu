import random

human = int(input(
    '\nLet\'s play Rock, Paper, Scissors!\n\n[0] - Rock\n[1] - Paper\n[2] - Scissors\n'))
ai = random.randint(0, 2)

if human == ai:
    print('TIE')
elif human == 0 and ai == 2 or human == 1 and ai == 0 or human == 2 and ai == 1:
    print('YOU WON!')
else:
    print('YOU LOSE!')

print(human, ai)

if human == 0:
    human = 'Rock'
elif human == 1:
    human = 'Paper'
else:
    human = 'Scissors'

if ai == 0:
    ai = 'Rock'
elif ai == 1:
    ai = 'Paper'
else:
    ai = 'Scissors'

print(f'You\'ve chosen {human} and AI has chosen {ai}.')
