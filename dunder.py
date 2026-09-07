# human readable printing with __str__
'''
class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.name} is studying {self.course}"


student1 = Student("Alex", "Python")

print(student1)
'''

# technical representation with __repr__

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def __repr__(self):
        return f"Student(name='{self.name}', course='{self.course}')"


student1 = Student("Alex", "Python")

print(repr(student1))

# measuring objects with __len__
class Team:
    def __init__(self, members):
        self.members = members
    def __len__(self):
        return len(self.members)
team1 = Team(["Alex", "Jordan", "Sam"])
print(len(team1))

# comparing objects with __eq__
class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


student1 = Student("Alex")
student2 = Student("Alex")

print(student1 == student2)

# Real world application
# creating a product class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ₦{self.price}"

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price})"

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price


product1 = Product("Laptop", 500000)
product2 = Product("Laptop", 500000)

print(product1)
print(repr(product1))

print(product1 == product2)