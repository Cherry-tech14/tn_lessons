# building the node class
'''
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

node_root = Node(4.50)
print(node_root.key)
print(node_root.left)

# inserting a cup(the sorting rule)
class CupNode:
    def __init__(self, price):
        self.price = price
        self.left = None
        self.right = None
def insert(node, price):
    
    if node is None:
        return CupNode(price)
        
    
    if price < node.price:

        node.left = insert(node.left, price)
    elif price > node.price:
        
        node.right = insert(node.right, price)
        
    return node  
root = CupNode(4.00)
insert(root, 3.00)
insert(root, 5.00)

print(root.left.price)
print(root.right.price)

# searching the tree
class CupNode:
    def __init__(self, price):
        self.price = price
        self.left = None
        self.right = None
def search(node, target):
    
    if node is None or node.price == target:
        return node
    if target < node.price:
        return search(node.left, target)
    else:
        return search(node.right, target)

result_node = search(root, target_price)     
root = CupNode(4.00)
insert(root, 3.00)
insert(root, 5.00)

found = search(root, 5.00)
print(found.price)
missing = search(root, 6.00)
print(missing)  


# Building the node class
class CupNode:
    def __init__(self, cup):
        self.cup = cup
        self.left = None
        self.right = None
cup = CupNode(50)

print(cup.cup)
print(cup.left)
print(cup.right)
'''

# inserting a cup(the sorting rule) using the insert() method
class CupNode:
    def __init__(self, cup):
        self.cup = cup
        self.left = None
        self.right = None

    def insert(self, cup):
        if cup < self.cup:
            if self.left is None:
                self.left = CupNode(cup)
            else:
                self.left.insert(cup)

        elif cup > self.cup:
            if self.right is None:
                self.right = CupNode(cup)
            else:
                self.right.insert(cup)

    def search(self, cup):
        if cup == self.cup:
            return True

        if cup < self.cup:
            if self.left is None:
                return False
            return self.left.search(cup)

        if cup > self.cup:
            if self.right is None:
                return False
            return self.right.search(cup)


root = CupNode(50)

root.insert(30)
root.insert(70)
root.insert(20)
root.insert(40)
root.insert(60)
root.insert(80)

print(root.search(60))
print(root.search(100))