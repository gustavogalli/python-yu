capitals = {
    'France': 'Paris',
    'Brazil': 'Brasília',
    'USA': 'Washington DC',
    'Italy': 'Rome',
    'Germany': 'Berlin'
}

travel_log = {
    'France': {
        'cities_visited': ['Paris', 'Le Havre', 'Dijon'],
        'total_visits': 12},
    'Brazil': ['Rio de Janeiro', 'São Paulo', 'Belo Horizonte']
}

print(travel_log['France']['total_visits'])

france_cities_visited = {
    'Paris': 3,
    'Le Havre': 1,
    'Dijon': 0
}

travel_wish = {
    'France': france_cities_visited,
    'Brazil': {'Rio de Janeiro': 4, 'São Paulo': 2}
}

print(travel_wish['France']['Paris'])
print(travel_wish['Brazil']['São Paulo'])

new_travel_log = [
    {
        'country': 'France',
        'cities_visited': ['Paris', 'Dijon'],
        'total_visits': 12
    },
    {
        'country': 'Brazil',
        'cities_visited': ['Manaus', 'Bertioga'],
        'total_visits': 7
    },
]

print(new_travel_log[0]['total_visits'])
