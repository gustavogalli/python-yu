fruits = {
    'apple': 'red fruit',
    'banana': 'yellow fruit',
}

# Retriving items
print(fruits['banana'])

# Adding items
fruits['pear'] = 'green fruit'
print(fruits)

# Create a new dictionary
new_dictionary = {}

# Wipe an existing dictionary
# fruits = {}

# Edit an item
fruits['apple'] = 'delicious red fruit'

# Loop through a dictionary
for key in fruits:
    print(key)
    print(fruits[key])
