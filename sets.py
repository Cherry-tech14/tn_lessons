'''
#set creation and uniqueness
# We try to add duplicate items
specials_tray = {"Cinnamon", "Cocoa", "Cinnamon", "Vanilla", "Cocoa"}

print(specials_tray) 

items = {"Cocoa", "Cocoa", "Vanilla"}
print(items)
print(len(items))

#membership testing(in and not in)
specials_tray = {"Cinnamon", "Cocoa", "Vanilla"}

has_cinnamon = "Cinnamon" in specials_tray  
has_nutmeg = "Nutmeg" in specials_tray
print(has_cinnamon)
print(has_nutmeg)      

toppings = {"Cinnamon", "Cocoa"}
print("Cinnamon" in toppings)
print("Nutmeg" not in toppings)

#set operations
my_tray = {"Cinnamon", "Cocoa"}
assistant_tray = {"Cocoa", "Nutmeg", "Vanilla"}

# 1. Union: Find all unique toppings available at our cart
all_toppings = my_tray | assistant_tray
print(all_toppings) # Output: {'Cinnamon', 'Cocoa', 'Nutmeg', 'Vanilla'}

# 2. Intersection: Find which toppings both trays have in common
matching_toppings = my_tray & assistant_tray
print(matching_toppings) # Output: {'Cocoa'}

set_a = {"Vanilla", "Mocha"}
set_b = {"Mocha", "Mint"}
print(set_a | set_b)
print(set_a & set_b)
'''
#set operations:difference
set_a = {"Vanilla", "Caramel", "Mocha"}
set_b = {"Caramel"}
print(set_a - set_b)