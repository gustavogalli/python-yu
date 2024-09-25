print('Welcome to the Treasure Island!\nYour mission is to find our treasure!')
direction = input(
    'First of all, choose a direction to go. Type "left" or "right":\n')

if direction == 'left':
    swin_wait = input(
        'Alright! Now you see a lake ahead. Would you "swim" or would you "wait"?\n')

    if swin_wait == 'wait':
        door = input('Perfect! Now you see three doors ahead. Choose one by typing "red", "yellow" or "blue"!\n')

        if door == 'yellow':
            print('Congratulations! You\'ve found our treasure!')
        else:
            print('Game over!')
            
    else:
        print('Game over!')

else:
    print('Game over!')