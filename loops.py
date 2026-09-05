'''
customers = ["Amaka", "Tunde", "Fatima"]
for customer in customers:
    print("Serving",customer)
    

count = 5
while count > 0:
    print("Countdown:", count)
    count = count - 1


for character in "Lagos":
    print(character)

for amount in [100, 250, 75, 400]:
    print("Transaction:", amount)

for number in [3, 8, 2]:
    print("Current number:", number)
    

transactions = [500, 1200, 300, 800]
total = 0
for amount in transactions:
    total = total + amount
print("Total:", total)


for i in range(5):
    print("steps:",i)
    

balance = 10000
withdrawal = 3000

while balance >= withdrawal:
    balance = balance-withdrawal
    print(balance)
    '''

for number in [1,2,3,4,5]:
    if number == 3:
        break
    print(number)

customers = ["Amaka", "Tunde", "Fatima","Chidi"]
search_name = "Fatima"
for customer in customers:
    if customer == search_name:
        print("Found", customer)
        break

for number in [1,2,3,4,5]:
    if number == 3:
        continue
    print(number)

customers = [
    {"name": "Amaka", "active": True},
    {"name": "Tunde", "active": False},
    {"name": "Fatima", "active": True},
]
for person in customers:
    if not person["active"]:
        continue
    print("process", person["name"])


