game_on = True

bidders = {}

def find_winner(bidders_list):
    winner_name = ''
    winner_bid = 0
    for bidder in bidders_list:
        if bidders_list[bidder] > winner_bid:
            winner_name = bidder
            winner_bid = bidders_list[bidder]

    print(f'{winner_name} is the winner bidding ${winner_bid}!')

while game_on:
    name = input('What is your name?\n')
    bid = int(input('What is your bid? $'))
    bidders[name] = bid
    answer = input('Wanna play again? Y/N\n').upper()
    if answer == 'N':
        game_on = False
        print('===================== GAME OVER =====================')

find_winner(bidders)
