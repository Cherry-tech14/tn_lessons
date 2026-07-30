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
'''

def make_custom_drink(base_drink, milk_type, sugar_packets):
    
    description = f"{base_drink} with {milk_type} milk"
    
    if sugar_packets > 0:
        description = description + f" and {sugar_packets} sugar packets"
        
    return description


order1 = make_custom_drink("Latte", "almond", 2)
order2 = make_custom_drink("Cappuccino", "whole", 0)

print(order1) 
print(order2) 