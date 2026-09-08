'''
# building the node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node_1 = Node("Alice")
print(node_1.data)
print(node_1.next)

# manually linking nodes
class CupNode:
    def __init__(self, name):
        self.customer_name = name
        self.next = None
cup_1 = CupNode("Alice")
cup_2 = CupNode("Bob")
cup_3 = CupNode("Charlie")


cup_1.next = cup_2 
cup_2.next = cup_3  
print(cup_1.next.customer_name)       
print(cup_1.next.next.customer_name) 

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

n1 = Node("A")
n2 = Node("B")
n1.next = n2
print(n1.next.val) 


# building the linked list manager class
class CupChain:
    def __init__(self):
        self.head = None  
        
    def append(self, name):
        new_cup = CupNode(name)
        
    
        if self.head is None:
            self.head = new_cup
            return
            
        
        current = self.head
        while current.next is not None:
            current = current.next  
            
        current.next = new_cup  

# traversing the chain
class CupChain:
    
    def traverse_and_print(self):
        current = self.head  
        
        while current is not None:
            print(f"Customer Cup: {current.customer_name}")
            current = current.next  
my_chain = CupChain()
my_chain.append("Alice")
my_chain.append("Bob")
my_chain.traverse_and_print()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node("Start")
head.next = Node("End")

current = head
while current is not None:
    print(current.data)
    current = current.next
    
# building the node class
class CupNode:
    def __init__(self, cup):
        self.cup = cup
        self.next = None
cup1 = CupNode("cup 1")

print(cup1.cup)
print(cup1.next)

# manually linking a nodes
class CupNode:
    def __init__(self, cup):
        self.cup = cup
        self.next = None


cup1 = CupNode("Cup 1")
cup2 = CupNode("Cup 2")
cup3 = CupNode("Cup 3")

cup1.next = cup2
cup2.next = cup3

print(cup1.cup)
print(cup1.next.cup)
print(cup1.next.next.cup)

# creating one node
class Node:
    def __init__(self, name):
        self.name = name
        self.next = None
node1 = Node("Mariam")

print(node1.name)
print(node1.next)

#creating 2 nodes
class Node:
    def __init__(self, name):
        self.name = name
        self.next = None
node1 = Node("Mariam")
node2 = Node("Alex")

print(node1.name)
print(node2.name)


# connecting a node
class Node:
    def __init__(self, name):
        self.name = name
        self.next = None
node1 = Node("Mariam")
node2 = Node("Alex")

node1.next = node2

print(node1.name)
print(node1.next.name)
'''

# creating 3 nodes
class Node:
    def __init__(self, name):
        self.name = name
        self.next = None


node1 = Node("Mariam")
node2 = Node("Alex")
node3 = Node("Jordan")

node1.next = node2
node2.next = node3

print(node1.name)
print(node1.next.name)
print(node1.next.next.name)