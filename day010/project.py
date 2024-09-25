def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


# Armazeando FUNÇÕES dentro de dicionários
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    num1 = float(input("What is the first number? "))
    for symbol in operations:
        print(symbol)

    on = True

    while on:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or 'n' to exit: ") == 'y':
            num1 = answer
        else:
            on = False
            calculator()  # call the self function (recursion)


calculator()
