'''
# import the whole module
import greetings

greetings.say_hello("Alex")

greetings.welcome("Alex")
greetings.say_goodbye("Alex")
'''

#import a specific function
from greetings import say_hello

say_hello("Alex")

# import multiple functions
from greetings import say_hello, say_goodbye

say_hello("Alex")
say_goodbye("Alex")

# import everything
from greetings import *

say_hello("Alex")
say_goodbye("Alex")
welcome("Alex")

# give a module an alias
import greetings as g

g.say_hello("Alex")
g.say_goodbye("Alex")
