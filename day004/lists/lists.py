# LISTS
fruits = ['apple', 'grape']

fruits.append('pineapple')
print(fruits)

fruits.pop(0)
print(fruits)

fruits.remove('grape')
print(fruits)

fruits.extend(['orange, banana, coconut'])
print(fruits)

vegetables = ['spinach', 'tomato', 'potato']

food = [fruits, vegetables]  # nested lists -> lists inside lists

print(food)
# [['pineapple', 'orange, banana, coconut'], ['spinach', 'tomato', 'potato']]
