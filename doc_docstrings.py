# example using docstring in code
'''
def greet(name):
    """Return a greeting for the given name."""
    return "Hello, " + name
print("Mariam")
greet("name")

# using triple quotes
def greet(name):
    """Return a greeting for a person's name."""
    return "Hello, " + name

print(greet("Alex"))


# how to view a docstring
def greet(name):
    """Return a greeting for a persons name."""
    return "Hello, " + name
print(greet. __doc__)


# Another way of viewing a docstring
def clean_cup(is_clean):
    """Reset the cup's cleanliness status."""
    return True
help(clean_cup)


# Google style docstrings
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of the two numbers.
    """
    return a + b


print(add_numbers(10, 5))


# Function docstring examples
# function with no parameters
def show_message():
    """Display a welcome message."""
    print("Welcome to Python")
show_message()


# function with parameters
def multiply(a: int, b: int) -> int:
    """multiply two numbers

    Args:
    a: The first number.
    b: The second number.

    Returns:
    The product of the two numbers.
    """
    return a * b
print(multiply(4, 5))

# function that can raise error
def divide(a: float, b: float) -> float:
    """Divide one number by another.

    Args:
        a: The number to divide.
        b: The number to divide by.

    Returns:
        The result of the division.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b


print(divide(10, 2))
'''

# class docstrings
class Student:
    """Represent a student."""
    def __init__(self, name, course):
        self.name = name
        self.course = course
student1 = Student("Alex", "Python")

print(student1.name)
print(student1.course)