'''
#stack
stack = []
stack.append("Cup A") 
stack.append("Cup B") 
print(stack.pop())  

#queue
queue = ["Cup A", "Cup B"]
print(queue.pop(0))
print(queue)


#stack
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
stack = Stack()
stack.push("Cup 1")
stack.push("Cup 2")
stack.push("Cup 3")

print(stack.items)

print(stack.pop())
print(stack.pop())
print(stack.pop)
'''

# queue
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
queue = Queue()
queue.enqueue("Person 1")
queue.enqueue("Person 2")
queue.enqueue("person 3")

print(queue.items)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

