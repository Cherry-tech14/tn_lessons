'''
def brew_coffee():
    print("Grinding espresso beans")
    print("coffee is ready")
brew_coffee() 

def greet_barista():
    print("Hello, barista!")
greet_barista()


#func with parameters
def print_label(name):
    print("Name on cup:" + name)
print_label("Alice")
print_label("Bob")


def order_drink(drink, size):
    print("Dispensing " + size + " " + drink)
order_drink("espresso", "large")   


#func with return values
def add_tax(subtotal):
    return subtotal * 1.08

final_total = add_tax(10.0)
print(final_total)

def make_custom_drink(base_drink, milk_type, sugar_packets):
    
    description = f"{base_drink} with {milk_type} milk"
    
    if sugar_packets > 0:
        description = description + f" and {sugar_packets} sugar packets"
        
    return description


order1 = make_custom_drink("Latte", "almond", 2)
order2 = make_custom_drink("Cappuccino", "whole", 0)

print(order1) 
print(order2) 


#functions with multiple parameters

def record_kiosk_order(name, drink, size, milk, sugar_packets):
    print(f"kiosk Receipt for {name}:")
    print(f"Item: {size} {drink}")
    print(f"Milk: {milk}")
    print(f"Sugar: {sugar_packets} packets")
record_kiosk_order("Alice", "latte", "large", "milk", "sugar" )  


def make_drink(name, drink):
    print(f"serving {drink} to {name}")
make_drink("Mariam", "Hollandia")  


def mix_ingredients(liquid, powder):
    print(f"Mixing {liquid} with {powder}")
mix_ingredients("milk", "cocoa")  

def mix_ingredients(liquid, powder):
    print("Mixing " + liquid + " with " + powder) 
mix_ingredients("milk", "cocoa")   


#positional arguments
def print_receipt(item, cost):
    print(item + ": #" + str(cost))
print_receipt("espresso", 4.50)   


#keyword arguments(arguments by name)
def brew_cup(drink, size, temperature):
    print(f"Brewing a {temperature} {size} {drink}")

brew_cup(temperature="iced", drink="cappuccino", size="medium")


def cup_label(name, drink):
    print(name + " ordered " + drink)
cup_label(drink="espresso", name="Alice")  
'''

#default parameter values
def process_order(name, drink, size="medium", milk="whole"):
    print(f"order for {name}: {size} {drink} with {milk} milk.")


