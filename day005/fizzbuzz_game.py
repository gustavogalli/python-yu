# fizz é divisível por 3
# buzz é divisível por 5
# fizzbuzz é divisível por 3 e 5

for number in range(1, 22):
    text = ''
    if number % 3 == 0 and number % 5 == 0:
        text = 'FizzBuzz'
        print(text)
    elif number % 3 == 0:
        text = 'Fizz'
        print(text)
    elif number % 5 == 0:
        text = 'Buzz'
        print(text)
    else:
        print(number)
