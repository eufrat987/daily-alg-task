# Hi, here's your problem today. This problem was recently asked by Apple:

# Implement a queue class using two stacks. A queue is a data structure 
# that supports the FIFO protocol (First in = first out). 
# Your class should support the enqueue and dequeue methods like a standard queue.

# Here's a starting point:

class Stack:
    def __init__(self):
        self.list = []
    def push(self, val):
        self.list.append(val)
    def pop(self):
        return self.list.pop()
    def isEmpty(self):
        return len(self.list) == 0

class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
    
    def enqueue(self, val):
        self.s1.push(val)

    def dequeue(self):
        if self.s2.isEmpty():
            while not self.s1.isEmpty():
                self.s2.push(self.s1.pop())
     
        return self.s2.pop()



q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print (q.dequeue())
print (q.dequeue())
print (q.dequeue())
# 1 2 3