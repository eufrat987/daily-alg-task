# Hi, here's your problem today. This problem was recently asked by Uber:

# Design a simple stack that supports push, pop, top, 
# and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

# Note: be sure that pop() and top() handle being called on an empty stack.

class minStack(object):
  def __init__(self):
      self.stack = []
      self.mini = []

  def push(self, x):
      self.stack.append(x)
      self.mini = [i for i in self.mini if i<x] + [x] + [i for i in self.mini if i>=x]

  def pop(self):
      x = self.stack.pop()
      self.mini.remove(x)
      return x

  def top(self):
      return self.stack[-1]

  def getMin(self):
      return self.mini[0]

x = minStack()
x.push(-2)
x.push(0)
x.push(-3)
print(x.getMin())
# -3
x.pop()
print(x.top())
# 0
print(x.getMin())
# -2