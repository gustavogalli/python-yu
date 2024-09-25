import random
from hangman_words import words

words_list = words
chosen_word = random.choice(words_list)
display = []
guesses = []
game_over = False
lives = 6

for _ in chosen_word:
    display.append('_')
print(display)

while not game_over:
    guess = input('\n\nChoose a letter: ').lower()

    if guess not in guesses:
        guesses.append(guess)

        for position in range(len(chosen_word)):
            letter = chosen_word[position]

            if letter == guess:
                display[position] = letter

        if guess not in display:
            lives -= 1
            if lives == 0:
                print('\nYOU LOSE. :(')
                print(f'The word was {chosen_word.upper()}')
                game_over = True

        print('LIVES =', lives)
        print(display)

        if "_" not in display:
            game_over = True
            print('\nYOU WON!!!')
    else:
        print(f'\nYou already guessed {guess} = {guesses}')

print('\n============== GAME OVER ==============')
