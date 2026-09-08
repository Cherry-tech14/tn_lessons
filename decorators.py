# functions as first class objects
'''
def greet():
    print("Hello!")

message = greet
message()


def greet():
    print("Hello")
my_function = greet
my_function()
'''

# functions can be passed to other functions
def greet():
    print("Hello!")


def run_function(function):
    function()


run_function(greet)

def say_hello():
    print("Hello")
def execute(function):
    print("Starting function")
    function()
    print("Function finished.")
execute(say_hello)