#list comprehensions
'''
standard_pumps = [1, 2, 3]
doubled_pumps = [p *2 for p in standard_pumps]

print(doubled_pumps)


prices = [3.00, 4.00, 5.00]
taxed_prices = [p *1.10 for p in prices]
print(taxed_prices)


# filtering inside list comprehensions

ordered_sizes = ["small", "large", "medium", "large", "small"]

large_only = [size for size in ordered_sizes if size == "large"]

print(large_only) 


volumes = [8, 12, 16, 20]
large_volumes = [v for v in volumes if v >= 16]
print(large_volumes)


# dictionary comprehensions
menu = {"Latte": 4.50, "Espresso": 3.50, "Mocha": 5.00}
discounted_menu = {drink: price - 0.50 for drink, price in menu.items()}
print(discounted_menu) 

stock = {"cups": 100, "lids": 150}
double_stock = {item: count * 2 for item, count in stock.items()}
print(double_stock)

# set comprehensions
messy_names = ["LATTE", "latte", "espresso", "latte"]
unique_clean = {name.lower() for name in messy_names}
print(unique_clean)

# list comprehensions
numbers = [1, 2, 3, 4, 5]

doubled = [number * 2 for number in numbers]

print(doubled)

names = ["john", "mary", "peter"]
upper_names = [name.upper() for name in names]
print(upper_names)


# dictionary comprehensions
names = ["Alex", "John", "Mary"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)

numbers = [1, 2, 3, 4]
squares = {number: number * number for number in numbers}
print(squares)


# set comprehensions
numbers = [1, 2, 3, 4, 5]
squares = {number * number for number in numbers}
print(squares)
'''

# real world application
# Or perhaps you only want products costing more than 100:
prices = [100, 250, 50, 300, 150]
expensive = [price for price in prices if price > 100]
print(expensive)