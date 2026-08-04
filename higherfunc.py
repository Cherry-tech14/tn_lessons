#lambda function
'''
double = lambda number: number * 2
num = int(input("Enter a number: "))
result = double(num)
print("The doubled number is:", result)

#map
menu_prices = [4.50, 3.50, 5.00]
updated_prices = list(map(lambda price: price + 0.5, menu_prices))
print(updated_prices)
'''

drinks = ["latte", "espresso", "mocha"]
loud_drinks = list(map(lambda d: d.upper(), drinks))

print(loud_drinks)