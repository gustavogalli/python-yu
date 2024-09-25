from data import data
from random import choice

score = 0
a = choice(data)
b = choice(data)

print('==================== HIGHER OR LOWER ====================')

game_on = True

while game_on:

    while a == b:
        b = choice(data)

    a_name = a['name']
    a_followers = a['followers']
    a_description = a['description']
    a_country = a['country']

    b_name = b['name']
    b_followers = b['followers']
    b_description = b['description']
    b_country = b['country']

    print(f'A: {a_name}, a {a_description} from {a_country}\nvs\nB: {b_name}, a {b_description} from {b_country}')
    guess = input("\nWho has more followers? 'A' or 'B' ").lower()
    if guess == 'a':
        if a_followers > b_followers:
            score += 1
            print(f'\nYou\'re right! Current score: {score}\n')
            b = choice(data)
        else:
            print(f'\nSorry, that\'s wrong. Final score: {score}')
            game_on = False
    else:
        if b_followers > a_followers:
            score += 1
            print(f'\nYou\'re right! Current score: {score}\n')
            a = b
            b = choice(data)
        else:
            print(f'\nSorry, that\'s wrong. Final score: {score}')
            game_on = False

print('======================= GAME OVER =======================')
