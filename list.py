#creating a list
'''
fruits = ["Apple", "Banana", "Orange"]
print(fruits)

syrub = ["Vanilla", "Mocha", "Mint"]
print(type(syrub))

#indexing in list
flavors = ["Vanilla", "Caramel", "Hazelnut", "Mocha", "Mint"]
print(flavors[4])

#negative indexing
flavors = ["Vanilla", "Caramel", "Hazelnut", "Mocha", "Mint"]
print(flavors[-1])

syrubs = ["Vanilla", "Caramel", "Hazelnut"]
print(syrubs[0])
print(syrubs[-1])

#slicing a list
flavors = ["Vanilla", "Caramel", "Hazelnut", "Mocha", "Mint"]
specialty_set = flavors[1:4]
print(specialty_set)


#method and mutability
flavors = ["Vanilla", "Caramel", "Hazelnut"]
flavors[1] = "Mocha"
print(flavors)

flavors = ["Vanilla", "Caramel", "Hazelnut"]
flavors[0] = "Vanilla-sugar"
print(flavors)


#Adding elements with append()
flavors = ["Vanilla", "Caramel"]
flavors.append("Mint")
print(flavors)

stock = ["Cup", "Lid"]
stock.append("Sleeve")
print(len(stock))


#removing elements elements with
flavors = ["Vanilla", "Caramel", "Hazelnut", "Mocha"]
popped_bottle = flavors.pop(1)
print(popped_bottle)
items.remove("Mocha")

flavors = ["Vanilla", "Caramel"]
if "Mint" in flavors:
    flavors.remove("Mint")
else:
    print("Mint is not on the rack. No action taken.") 
    
items = ["Vanilla", "Mocha", "Mint"]
last_item = items.pop()
print(last_item)
items.remove("Vanilla")
print(items)  


flavors = ["Vanilla", "Caramel", "Hazelnut"]
flavors.sort()
print(flavors)

prices = [4.50, 3.50, 5.00]
prices.sort()
print(prices)


# slicing in list
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])

# sort
numbers = [5, 2,8, 1, 3]
numbers.sort()
print(numbers)

# list methods(append)
fruits = ["apple", "banana",]
fruits.append("orange")
print(fruits)

names = ["Mariam", "Joy", "Blessing"]
names.append("Emmanuel")
print(names)

# insert
fruits = ["apple", "banana",]
fruits.insert(1,"orange")
print(fruits)

# remove()
fruits = ["apple", "banana", "orange"]
fruits.remove("orange")
print(fruits)

# pop()
fruits = ["apple", "banana", "orange"]
fruits.pop(1)
print(fruits)

# reverse()
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)
'''

# mutability
names = ["Mariam", "John"]
names.append("David")
names[0] = "Sarah"
print(names)

# Tuples

