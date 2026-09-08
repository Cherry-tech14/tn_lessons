# iterables
'''
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

word = "Python"
for letter in word:
    print(letter)
    

# iterators
numbers = [10, 20, 30]
iterator = iter(numbers)
print(iterator)


# getting the next item
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
'''

# building a custom iterator
class Orderstream:
    def __init__(self):
        self.order_number = 1
    def __iter__(self):
        return self
    def __next__(self):
        order = f"order{self.order_number}"
        self.order_number += 1
        return order
stream = Orderstream()
print(next(stream))
print(next(stream))
print(next(stream))
print(next(stream))
print(next(stream))
