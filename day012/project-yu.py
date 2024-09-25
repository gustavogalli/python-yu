from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_guess(answer, guess, turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif answer > guess:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The number is {answer}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()

    guess = 0
    while answer != guess:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_guess(answer, guess, turns)

        if turns == 0:
            print('You run out of guesses! Too bad!')
            return  # exit the loop
        elif guess != answer:
            print('Guess again.')

    print('================== GAME OVER ==================')


game()
