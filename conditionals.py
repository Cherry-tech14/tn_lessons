'''
drink = "Coffee"
temperature = 100

if drink == "Green Tea":
     temperature = 80 
elif drink == "Coffee":
     temperature = 90
else:
     temperature = 100
print(temperature)


# Boolean context contexts and truthiness
if 0:
     print("Zero is truthy")
else:
     print("Zero is falsey")

name = input("Enter your name:")
if name:
     print("Hello,", name)
else:
     print("You did not enter a name")   
     

# if/else/ elif statement statement
balance = 12000
if balance > 5000:
    print("You can make a large transfer") 
print("End of check")

balance = 2000
if balance > 5000:
     print("Large balance")
else:
     print("Balance is not large")

distance = 7

if distance <= 5:
    fee = 1000
elif distance <= 10:
    fee = 1500
elif distance <= 20:
    fee = 2500
else:
    fee = 4000

print("Delivery fee:", fee)

score = 75

if score >= 80:
    print("Excellent")
elif score >= 50:
    print("Pass")
else:
    print("Fail")
    

balance = 4500
account_locked = False

if account_locked:
    print("Account locked")
elif balance <= 0:
    print("No funds")
elif balance < 5000:
    print("Low balance warning")
else:
    print("Balance is healthy")
    '''

balance = 12000
account_locked = False
amount = 3000
if balance <= 0:
     print("Balance is zero")
elif account_locked:
     print("Account locked")
elif amount > balance:
     print("insufficient balance")
else:
     print("Processing withdrawal")

age = 20
has_ticket = False
has_id = True

if age < 18:
    print("You are too young.")
elif not has_ticket:
    print("You need a ticket.")
elif not has_id:
    print("You need an ID.")
else:
    print("You can enter.")

