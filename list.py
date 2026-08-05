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
'''

flavors = ["Vanilla", "Caramel", "Hazelnut"]
flavors.sort()
print(flavors)

prices = [4.50, 3.50, 5.00]
prices.sort()
print(prices)

