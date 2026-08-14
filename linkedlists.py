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
'''

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