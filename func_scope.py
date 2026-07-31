#local scope
'''

def make_latte():
    coffee_grams = 18
    milk_ounces = 8
    print(f"Brewing with {coffee_grams}g of coffee and {milk_ounces}oz of milk.")
make_latte()  

def steam_milk():
    temp = 65
    print(f"Milk steamed to {temp} degrees")
    return temp
final_temp = steam_milk()
print(final_temp)


def test_scope():
    secret_recipe = "vanilla syrup"
    print(secret_recipe)
    
test_scope()


#global scope
menu_price = 4.50

def serve_customer(name):
    print(f"charging {name} #{menu_price:.2f} for their latte.")
serve_customer("Alice") 

shop_name = "Espresso cart"
def print_shop():
    print("welcome to " + shop_name)   
print_shop()    

#global keyword
menu_price = 4.50
def update_price(new_price):
    global menu_price
    menu_price = new_price
    print(f"whiteboard price updated to #{menu_price:.2f}")
    update_price(5.00)
print(f"Current menu price is now: #{menu_price:.2f}") 

total_sales = 0.0
def record_sales(amount):
    global total_sales
    total_sales = total_sales + amount
    print(f"Sales recorded: # {amount:.2f}")
record_sales(4.50)
print(f"Register total sales: # {total_sales:.2f}")

#variable lifetime: local variables & global variables
global_sales = 0
def make_drink():
    local_count = 0
    global global_sales

    local_count = local_count + 1
    global_sales = global_sales + 1
    print(f"Local: {local_count}, Global: {global_sales}")
make_drink()
make_drink()    


#non_local keyword
def run_coffee_cart():
    current_order = "Espresso"
    def change_order(new_drink):
        nonlocal current_order
        current_order = new_drink
        print(f"Order updated to: {current_order}")
    change_order("Latte")
    print(f"Final cart order: {current_order}")  
run_coffee_cart() 
'''
def outer():
    x = "original"
    def inner():
        nonlocal x
        x = "modified"
    inner()
    print(x)
outer()    




