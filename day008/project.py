alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cypher(msg, shift, choice):
    if choice == 'decode':
        alphabet.reverse()

    for i in range(len(alphabet)):
        alphabet.append(alphabet[i])

    new_msg = ''

    for char in msg:
        if char in alphabet:
            shift = shift % 26

            index = alphabet.index(char)
            new_msg += alphabet[index + shift]
        else:
            new_msg += char

    print(new_msg)


game_on = True

while game_on:
    good_choice = False
    while not good_choice:
        choice = input('Encode or decode?\n')
        if choice == 'encode' or choice == 'decode':
            good_choice = True
        else:
            print('Please, type "encode" or "decode".\n')
    msg = input('Type a message:\n')
    shift = int(input('How much shift?\n'))
    cypher(msg, shift, choice)

    answer = input('Want to keep playing? Y/N\n').upper()
    if answer == 'N':
        game_on = False
    else:
        game_on = True

print('==================== GAME OVER ====================')
