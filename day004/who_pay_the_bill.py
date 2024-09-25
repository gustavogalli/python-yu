import random

people = []  # list

people.append('Anne')
people.extend(['Peter', 'John'])
people.pop(0)
people.extend(['Catharine', 'Dwayne', 'Bella'])

chosen = people[random.randint(0, len(people) - 1)]

print(f'{chosen} is going to pay the bill!')
