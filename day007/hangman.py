import random
words = ['apple', 'motorcycle', 'airplane', 'crush', 'wonder', 'amazing', 'dictionary', 'bubbles', 'wizard', 'magic']
word = random.choice(words)
word_list = []
hidden_word = []
for letter in word:
    word_list.append(letter)
    hidden_word.append('_')

game_over = False
acertos = 0

while not game_over:
    print(hidden_word)
    guess = input('\n\nChoose a letter: ')
    if guess in word_list:
        print('\nAcertou!!!')

        for n in range(0, len(word_list)):
            if guess == word_list[n]:
                hidden_word[n] = guess
        
        acertos += word_list.count(guess)



    else:
        print('errou\n\n')

    if acertos == len(word_list):
        game_over = True
        print('==================== PARABÉNS! ====================')