# Global variables are defined outside any function
# Local variables (and also functions) are defined withing functions, and cannot be accessed outside

enemies = 1  # global scope


def increase_enemies():
    enemies = 2  # local scope
    print(f'Enemies inside function: {enemies}')  # 2


increase_enemies()
print(f'Enemies outside function: {enemies}')  # 1


# In case we want to modify a global variable (NOT RECOMMENDED),
# we define it within the function with GLOBAL:

def increase_enemies():
    global enemies  # <- like that
    enemies = 3
    print(f'Enemies inside function: {enemies}')  # 3


increase_enemies()
print(f'Enemies outside function: {enemies}')  # 3
