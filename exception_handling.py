# code with exception error
'''
print("Program started")

number = int("Hello")
print("Program finished")


# try/except _catching exceptions
try:
    number = int("hello")
    print(number)
except:
    print("Something went wrong")
    

try:
    age = int(input("Enter your age: "))
    print("your age is", age)
except:
    print("Please enter a valid number.")
    

try:
    num = int(input("Enter a number: "))
    print("Your number is", num)
except:
    print("invalid number")
    

# Catching specific exceptions
# Catching ValueError
try:
    number = int("hello")
    print(number)
except ValueError:
    print("That is not a valid number.")

# Catching multiple specific exceptions
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")


# IndexError
fruits = ["apple", "banana", "orange"]

try:
    print(fruits[5])
except IndexError:
    print("That position does not exist.")
'''
numbers = [10, 20, 30]

try:
    index = int(input("Enter an index: "))
    print(numbers[index])

except ValueError:
    print("Please enter a number.")

except IndexError:
    print("That index does not exist.")