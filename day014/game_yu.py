from data import data
import random


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f'{account_name}, a {account_descr}, from {account_country}'


def check_answer(guess, a_followers, b_followers):
    """Takes the user guess and followers quantity and returns if they got it right."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


print('HIGHER OR LOWER')
score = 0
game_on = True
account_b = random.choice(data)

while game_on:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f'Compare A: {format_data(account_a)}')
    print('vs')
    print(f'Against B: {format_data(account_b)}')

    guess = input("Who has more followers? 'A' or 'B' ").lower()
    a_followers = account_a['followers']
    b_followers = account_b['followers']

    is_correct = check_answer(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f'You are right! Current score: {score}')
    else:
        print(f'Sorry, that\'s wrong. Final score: {score}')
        game_on = False
