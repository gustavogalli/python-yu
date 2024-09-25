from dictionaries import menu, machine

QUARTER_VALUE = 0.25
DIME_VALUE = 0.10
NICKEL_VALUE = 0.05
PENNY_VALUE = 0.01

machine_on = True

print("""
 _____        __  __                                 _     _            
/  __ \      / _|/ _|                               | |   (_)           
| /  \/ ___ | |_| |_ ___  ___   _ __ ___   __ _  ___| |__  _ _ __   ___ 
| |    / _ \|  _|  _/ _ \/ _ \ | '_ ` _ \ / _` |/ __| '_ \| | '_ \ / _ |
| \__/\ (_) | | | ||  __/  __/ | | | | | | (_| | (__| | | | | | | |  __/
 \____/\___/|_| |_| \___|\___| |_| |_| |_|\__,_|\___|_| |_|_|_| |_|\___|
                                                                        
                                                                        
""")


def print_report():
    water = machine['ingredients']['water']
    coffee = machine['ingredients']['coffee']
    milk = machine['ingredients']['milk']
    money = machine['money']
    return f'\n====== REPORT ======\nWater ...... {water}ml\nCoffee ..... {coffee}g\nMilk ....... {milk}ml\nMoney ...... ${money}\n'


def turn_off():
    global machine_on
    machine_on = False
    return """
                                 _      _                        __   __ 
                                | |    (_)                      / _| / _|
         _ __ ___    __ _   ___ | |__   _  _ __    ___    ___  | |_ | |_ 
        | '_ ` _ \  / _` | / __|| '_ \ | || '_ \  / _ \  / _ \ |  _||  _|
        | | | | | || (_| || (__ | | | || || | | ||  __/ | (_) || |  | |  
        |_| |_| |_| \__,_| \___||_| |_||_||_| |_| \___|  \___/ |_|  |_|  
                                                                        
        """


def process_choice(choice):
    if choice == 'report':
        return print_report()
    elif choice == 'off':
        return turn_off()
    else:
        return has_resources(choice)


def has_resources(order):
    for ingredient in menu[order]['ingredients']:
        for machine_ingredient in machine['ingredients']:
            if ingredient == machine_ingredient:
                qtd_ingrediente_cafe = menu[order]['ingredients'][ingredient]
                qtd_ingrediente_maquina = machine['ingredients'][machine_ingredient]
                if qtd_ingrediente_cafe > qtd_ingrediente_maquina:
                    return f'Sorry, we don\'t have enough {ingredient} to make a {order}.'
                else:
                    return check_payment(order)


def check_payment(order):
    coffee_price = menu[order]['price']

    print(f'\nA {order} costs ${coffee_price}.')

    print('\nPlease insert coins:')
    quarters = float(input('How many quarters? ($0.25) '))
    dimes = float(input('How many dimes? ($0.10) '))
    nickels = float(input('How many nickels? ($0.05) '))
    pennies = float(input('How many pennies? ($0.01) '))

    payment = quarters * QUARTER_VALUE + dimes * DIME_VALUE + \
        nickels * NICKEL_VALUE + pennies * PENNY_VALUE

    print(f'\nYou paid ${round(payment, 2)}')

    if payment >= coffee_price:
        print(f'\nHere\'s your change: ${round(payment - coffee_price, 2)}')
        return make_coffee(order)
    else:
        return f'\nSorry, that\'s not enough money. Money refunded.'


def make_coffee(choice):
    if menu[choice]['ingredients']['water'] > machine['ingredients']['water'] or menu[choice]['ingredients']['coffee'] > machine['ingredients']['coffee'] or menu[choice]['ingredients']['milk'] > machine['ingredients']['milk']:
        # print('Sorry, there is not enough water!')
        return 'Sorry, there is not enough ingredients!'
    else:
        machine['ingredients']['water'] -= menu[choice]['ingredients']['water']
        machine['ingredients']['coffee'] -= menu[choice]['ingredients']['coffee']
        machine['ingredients']['milk'] -= menu[choice]['ingredients']['milk']
        machine['money'] += menu[choice]['price']

        return f'Here is your {choice}. Enjoy!'


while machine_on:
    choice = input('\nWhat would  you like? (espresso/latte/cappuccino): ')
    print(process_choice(choice))
