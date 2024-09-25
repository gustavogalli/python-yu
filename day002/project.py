print('Welcome to the calculator!')
bill = float(input('What was the total bill? $'))  # 124.56
tip = float(input('How much tip would you like to give? 10, 12, or 15? '))  # 12
people = int(input('How many people to split the bill? '))  # 7

splitedBill = bill / people
splitedTip = tip * bill / 100 / people
result = round(splitedBill + splitedTip, 2)

print(f'Each people should pay: ${result}')  # 19.93
