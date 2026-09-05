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


#default parameter values
def process_order(name, drink, size="medium", milk="whole"):
    print(f"order for {name}: {size} {drink} with {milk} milk.")
process_order("Mariam", "fanta") 


def sprinkle_sugar(packets=1):
    print("Adding " + str(packets) + " sugar packets.")
sprinkle_sugar()    
sprinkle_sugar(3)


#mixing positional and keyword arguments
def brew_custom_cup(drink, size, temperature, milk="whole", sugar=0):
    print(f"Making a {temperature} {size} {drink} with {milk} milk.")
brew_custom_cup("Latte", "large", "hot", milk="almond", sugar=1)

def greet(name):
    print("Hello", name)
greet("Mariam")

# local variable
def greet():
    name = "Mariam"
    print(name)
greet()

# global variable
name = "Mariam"
def greet():
    print(name)
greet()

def say_hello():
    print("Hello!")
def execute(function):
    function()
execute(say_hello)


# using lambda function
numbers = [1, 2, 3, 4]
result = map(lambda x: x * 2, numbers)
print(list(result))

# using map()
names = "Mariam", "Aisha", "John"
result = map(lambda name: name.upper(), names)
print(list(result))
'''

# using filter()
names = ["Mariam", "John", "Michael", "Ada"]
result = filter(lambda name: len(name) > 4, names)
print(list(result))