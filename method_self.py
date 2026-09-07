# defining instance methods
'''
class Dog:
    def bark(self):
        print("woof woof")
dog1 = Dog()
dog1.bark()

# the role of self in methods
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof! My name is", self.name)


dog1 = Dog("Buddy")
dog2 = Dog("Max")

dog1.bark()
dog2.bark()

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount


account = BankAccount(100)

print(account.balance)

account.deposit(50)

print(account.balance)


# Real world application
# creating a user account: the user might have username, email, password

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def change_email(self, new_email):
        if "@" in new_email:
            self.email = new_email
            print("Email updated")
        else:
            print("Invalid email")
user1 = User("alex123", "alex@example.com")

user1.change_email("new@example.com")

print(user1.email)
'''

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawal successful")
        else:
            print("Insufficient funds")


account = BankAccount(1000)

account.deposit(500)
print(account.balance)

account.withdraw(300)
print(account.balance)

account.withdraw(2000)
print(account.balance)