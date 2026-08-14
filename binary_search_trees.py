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
''' 
