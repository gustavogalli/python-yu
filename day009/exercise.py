country = input()
visits = int(input())
list_of_cities = eval(input())

travel_log = [
    {
        'country': 'France',
        'visits': 12,
        'cities': ['Paris', 'Lille', 'Dijon']
    },
    {
        'country': 'Germany',
        'visits': 5,
        'cities': ['Berlin', 'Hamburg', 'Stuttgart']
    }
]


def add_new_country(new_country, new_visits, list):
    new_country = {'country': new_country, 'visits': new_visits, 'cities': list}
    travel_log.append(new_country)


# add new cities to the travel_log
add_new_country(country, visits, list_of_cities)
print(f"Ive been to {travel_log[2]['country']} {travel_log[2]['visits']} times")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
