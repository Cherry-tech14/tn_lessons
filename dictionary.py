#creating a dictionary
'''
menu = {
    "Latte": 4.50,
    "Espresso": 3.50
}
print(menu) 

inventory = {"cups": 100, "lids":150}
print(type(inventory))


#accessing values by key
menu = {
    "Latte": 4.50,
    "Espresso": 3.50
}
latte_price = menu["Latte"]
print(latte_price) 

stock = {"cups":100, "lids":150}
print(stock["cups"])


#updating and adding values
menu = {
    "Latte": 4.50,
    "Espresso": 3.50
}

# 1. Update an existing price (Latte increases to 5.00)
menu["Latte"] = 5.00
# 2. Add a brand-new drink to the board (Chai is added)
menu["Chai"] = 4.00

print(menu)

kiosk = {"status": "OFF"}
kiosk["status"] = "ON"
kiosk["operator"] = "Robot"
print(kiosk)
'''
#handling key errors safely
menu = {"Latte": 4.50}
print(menu.get("Chai"))
print(menu.get("Chai", 3.00))