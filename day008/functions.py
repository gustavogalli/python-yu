def greet_with(n, l):
    print(f'Hi, {n}. So, are you from {l}?')


name = input('What is your name?\n')
location = input('Where are you from?\n')

# POSITION ARGUMENTS
greet_with(name, location)

# KEYWORD ARGUMENTS
# podemos passar o PARÂMETRO (nome do campo) e o ARGUMENTO (valor do campo) juntos:
greet_with(l=location, n=name)
