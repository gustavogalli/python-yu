# # Describe the problem
# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it.")
# my_function()

# # Reproduce the bug
# from random import randint
# dice_imgs = ['1', '2', '3', '4', '5', '6']
# dice_num = randint(1, 6)  # index 6 is out of range
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What is your year of birth? "))
# if year > 1980 and year < 1994:
#     print("You are a milennial.")
# elif year > 1994:
#     print("You are Gen Z.")

# # Fix the Errors
# age = input("How old are you? ")
# if age > 18:
#     print("You can drive at age {age}.")

# # PRINT is your friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) # Wrong assignment
# total_words = pages * word_per_page
# print(total_words)

# Use a debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
