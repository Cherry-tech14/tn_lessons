# creating a subclass
'''
class Animal:
    def eat(self):
        print("The animal is eating")
class Dog(Animal):
    pass

dog1 = Dog()
dog1.eat()

class Animal:
    def eat(self):
        print("The animal is eating")

    def sleep(self):
        print("The animal is sleeping")


class Dog(Animal):
    pass


dog1 = Dog()

dog1.eat()
dog1.sleep()


# overriding parent methods
class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("The dog says woof")

animal1 = Animal()
dog1 = Dog()

animal1.speak()
dog1.speak()


# The role of super() in methods

class Animal:
    def speak(self):
        print("The animal makes a sound")
class Dog(Animal):
    def speak(self):
        super().speak()
        print("The dog says woof")
dog1 = Dog()
dog1.speak()
'''

# real world application
# imagine a company has general employees

class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(self.name, "is working")


class Manager(Employee):
    def work(self):
        super().work()
        print(self.name, "is managing the team")


class Developer(Employee):
    def work(self):
        super().work()
        print(self.name, "is writing code")


manager1 = Manager("Alex")
developer1 = Developer("Jordan")

manager1.work()
developer1.work()
