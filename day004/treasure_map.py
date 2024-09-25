line1 = [' ', ' ', ' ']
line2 = [' ', ' ', ' ']
line3 = [' ', ' ', ' ']
map = [line1, line2, line3]

print('Hiding your treasure! X marks the spot!')

letter = input('Type a letter: A, B or C\n') # B
number = input('Type a letter: A, B or C\n') # 2

abc = ['a', 'b', 'c']
nums = ['1', '2', '3']

letter_position = abc.index(letter)
number_position = nums.index(number)

map[letter_position][number_position] = 'X'

print(f'{line1}\n{line2}\n{line3}')
