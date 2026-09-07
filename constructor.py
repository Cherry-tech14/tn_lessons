# the magic of the constructor(init)
'''
class Student:
    def __init__(self):
        print("A new student has been created!")


student1 = Student()

class Dog:
    def __init__(self):
        print("A new dog has been created")
dog1 = Dog()
dog2 = Dog()

# initializing with default values

class Student:
    def __init__(self):
        self.name = "Unknown"
        self.course = "Not assigned"
student1 = Student()

print(student1.name)
print(student1.course)
'''

# initializing with passed arguments
class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


phone1 = Phone("Samsung", 300000)
phone2 = Phone("Apple", 500000)

print(phone1.brand)
print(phone1.price)

print(phone2.brand)
print(phone2.price)

# Real world application
# imagine we are creating a bank account program, every bank account should have information such as:
# * account holder
# * balance

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance


account1 = BankAccount("Alex", 1000)
account2 = BankAccount("Jordan", 2500)

print(account1.account_holder)
print(account1.balance)

print(account2.account_holder)
print(account2.balance)


