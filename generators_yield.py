# getting value from the generator
'''
def get_numbers():
    yield 1
    yield 2
    yield 3
numbers = get_numbers()
print(next(numbers))
print(next(numbers))
print(next(numbers))


def get_fruits():
    yield "apple"
    yield "banana"
    yield "orange"

fruits = get_fruits()

print(next(fruits))
print(next(fruits))
print(next(fruits))

# using a for loop with a generator
def get_numbers():
    yield 10
    yield 20
    yield 30

for number in get_numbers():
    print(number)
    

# building coffee order generators
def coffeeorders():
    yield "coffee order 1"
    yield "coffee order 2"
    yield "coffee order 3"
    yield "coffee order 4"
    yield "coffee order 5"
coffee = coffeeorders()

print(next(coffee))
print(next(coffee))
print(next(coffee))
print(next(coffee))
print(next(coffee))


# making it with a loop
def coffee_orders():
    for number in range(1, 6):
        yield f"coffee order {number}"
for order in coffee_orders():
    print(order)
    '''

def number_generator():
    for number in range(1, 1000001):
        yield number
for numbers in number_generator():
    print(numbers)

