from dictionaries import machine, menu


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= machine['ingredients'][item]:
            print(f'Sorry, there\'s is not enough {item}')
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print('Please, insert the coins:')
    total = int(input('How many quarters? ')) * 0.25
    total += int(input('How many dimes? ')) * 0.10
    total += int(input('How many nickels? ')) * 0.05
    total += int(input('How many pennies? ')) * 0.01
    return total


def is_transaction_sucessfull(money_received, drink_cost):
    """Returns True when the payment is accepted, False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f'Here is ${change} in change.')
        machine['money'] += drink_cost
        return True
    else:
        print(f'Sorry, there\'s not enough money. Money refunded.')
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the machine."""
    for item in order_ingredients:
        machine['ingredients'][item] -= order_ingredients[item]
    print(f'Here is your {drink_name}! Enjoy!')


is_on = True

while is_on:
    choice = input('What would you want? (espresso/latte/cappuccino): ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {machine['ingredients']['water']}")
        print(f"Milk: {machine['ingredients']['milk']}")
        print(f"Coffee: {machine['ingredients']['coffee']}")
        print(f"Money: ${machine['money']}")
    else:
        drink = menu[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_sucessfull(payment, drink['price']):
                make_coffee(choice, drink['ingredients'])
