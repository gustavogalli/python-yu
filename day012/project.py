import random

print("""
   ___                          _____ _                   __                 _               
  / _ \_   _  ___  ___ ___     /__   \ |__   ___       /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|      / /\/ '_ \ / _ \     /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_  | |_| |  __/\__ \__ \     / /  | | | |  __/    / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/     \/   |_| |_|\___|    \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|   
                                                                                             
""")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0

if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5

number = random.randint(1, 100)
guess = 0
game_on = True

if number != guess and attempts > 0:
    game_on = True

while game_on:
    print(f"\nYou have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess > number:
        print('\nToo high.')
        attempts -= 1
    elif guess < number:
        print('\nToo low.')
        attempts -= 1
    else:
        print(f'\nVery good! You guessed the number {number} correctly!')
        game_on = False

    if attempts == 0:
        print(f"You don't have more lives. Too bad! :(")
        game_on = False

print("""\n                                      
  __ _  __ _ _ __ ___   ___      _____   _____ _ __ 
 / _` |/ _` | '_ ` _ \ / _ \    / _ \ \ / / _ \ '__|
| (_| | (_| | | | | | |  __/   | (_) \ V /  __/ |   
 \__, |\__,_|_| |_| |_|\___|    \___/ \_/ \___|_|   
 |___/                                              
                                                   
""")
