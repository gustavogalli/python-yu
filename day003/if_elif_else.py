print('Welcome to the rollercoaster!')
height = float(input('What is your height in cm? '))

if height >= 120:
    print('You can ride it!')

    bill = 0
    age = int(input('What is your age? '))

    if age < 12:
        print('Please, pay $5.')
        bill += 5

    elif age <= 18:
        print('Please, pay $7.')
        bill += 7

    elif age >= 45 and age <= 65:
        print('Good news! You don\'t need to pay for it!')

    else:
        print('Please, pay $12.')
        bill += 12

    wants_photo = input('Do you want a photo taken for $3? Y or N ').upper()

    if wants_photo == 'Y':
        bill += 3

    print(f'Your final bill is ${bill}.')

else:
    print('Sorry, you have to be taller to ride it!')
