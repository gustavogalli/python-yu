import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

password = ''
password_list = []
new_password_list = []

print('Welcome to the PyPassword Generator!')
n_letters = int(input('How many letters would you like in your password?\n'))
n_symbols = int(input('How many symbols?\n'))
n_numbers = int(input('How many numbers?\n'))

# populate password_list
for l in range(0, n_letters):
    password_list.append(letters[random.randint(0, len(letters)) - 1])

for s in range(0, n_symbols):
    password_list.append(symbols[random.randint(0, len(symbols)) - 1])

for n in range(0, n_numbers):
    password_list.append(numbers[random.randint(0, len(numbers)) - 1])

# randomly populating new_password_list
for item in range(0, len(password_list)):
    random_number = random.randint(0, len(password_list) - 1)
    new_password_list.append(password_list.pop(random_number))

for char in new_password_list:
    password += char

print(f'Here is your password: {password}')
