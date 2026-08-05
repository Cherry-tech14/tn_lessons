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


drinks = ["latte", "espresso", "mocha"]
loud_drinks = list(map(lambda d: d.upper(), drinks))

print(loud_drinks)


numbers = [2, 4, 6]
result = list(map(lambda n: n * 3, numbers))
print(result)

#filter
numbers = [2, 4, 6]
result = list(filter(lambda m: m > 3, numbers))
print(result)

prices = [1.50, 5.00, 3.25, 6.00]
cheap_prices = list(filter(lambda p: p < 4.00, prices))
print(cheap_prices)


#sorted
numbers = [8, 2, 6, 1]
print(sorted(numbers))
'''
menu_items = [
    {"name": "Mocha", "price":5.00},
    {"name": "Espresso", "price":3.50},
    {"name": "Latte", "price":4.50}
    ]
sorted_by_price = sorted(menu_items, key=lambda item: item["price"])
print(sorted_by_price)
