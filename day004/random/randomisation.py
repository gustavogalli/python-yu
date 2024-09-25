import random
from pi import pi_value  # importing a single variable
import color            # importing the whole module

print(pi_value)         # acessing the variable itself
print(color.blue)       # acessing the module variable


random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()  # 0.0 to 1.0   -    not including 1.0
print(random_float)
