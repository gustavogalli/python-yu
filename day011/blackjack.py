import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
chips = 100
pot = 0

def game(chips, pot):
    player_hand = []
    computer_hand = []

    player_hand_total = 0
    computer_hand_total = 0

    player_hand.append(random.choice(deck))
    player_hand.append(random.choice(deck))
    computer_hand.append(random.choice(deck))
    computer_hand.append(random.choice(deck))

    for card in player_hand:
        player_hand_total += card

    for card in computer_hand:
        computer_hand_total += card

    print(f'\n----------------- LET\'S PLAY ----------------')
    bet = int(input(f'You have {chips} chips. How much will you bet? '))
    chips -= bet
    pot += bet

    round_on = True
    while round_on:
        print(f'\n{player_hand} Your total: {player_hand_total}')
        print(f'[{computer_hand[0]}, ?]')
        if player_hand_total == 21:
            print(f'\nYOU WON!!! BLACKJACK!!!')
            chips += pot * 2
            print(f'Total chips: {chips}')
            round_on = False
        else:
            bet = int(input('\nHow much to raise your bet? '))
            chips -= bet
            pot += bet
            answer = input("\nWanna buy a card? y/n ")

            if answer == 'y':
                new_card = random.choice(deck)
                if new_card == 11 and player_hand_total + 11 > 21:
                    new_card = 1
                player_hand.append(new_card)
                player_hand_total += new_card

                if player_hand_total > 21:
                    print(
                        f'\n------------------ BUST! {player_hand_total} -----------------')
                    print(f'\n{player_hand} Your total: {player_hand_total}')
                    print(f'\n--------------- COMPUTER WINS ---------------')
                    print(f'Total chips: {chips}')
                    pot = 0
                    round_on = False
            else:
                computer_keep_playing = True
                while computer_keep_playing:
                    if computer_hand_total < 17:
                        new_card = random.choice(deck)
                        computer_hand.append(new_card)
                        computer_hand_total += new_card
                    else:
                        computer_keep_playing = False

                print('\n----------------- RESULTADO -----------------')
                print('\nPLAYER:', player_hand, player_hand_total)
                print('COMPUTER:', computer_hand, computer_hand_total)
                if player_hand_total == computer_hand_total:
                    print('\n-------------------- DRAW -------------------')
                    chips += pot
                    pot = 0
                    print(f'Total chips: {chips}')
                elif player_hand_total > computer_hand_total or computer_hand_total > 21:
                    print('\n---------------- PLAYER WINS ----------------')
                    chips += pot * 2
                    pot = 0
                    print(f'Total chips: {chips}')
                else:
                    print('\n--------------- COMPUTER WINS ---------------')
                    print(f'Total chips: {chips}')
                    pot = 0
                round_on = False

    play_again = input('\nWanna play again? y/n ')
    if play_again == 'y':
        game(chips, pot)

game(chips, pot)
print('\n================= GAME OVER =================')
