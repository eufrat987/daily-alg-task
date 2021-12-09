# Hi, here's your problem today. This problem was recently asked by Microsoft:

# A k-ary tree is a tree with k-children, and a tree is symmetrical 
# if the data of the left side of the tree is the same as the right side of the tree.

# Here's an example of a symmetrical k-ary tree.
#         4
#      /     \
#     3        3
#   / | \    / | \
# 9   4  1  1  4  9
# Given a k-ary tree, figure out if the tree is symmetrical.

# Here is a starting point:

class Node():
  def __init__(self, value, children=[]):
    self.value = value
    self.children = children

def helper(nodeList):
  if len(nodeList) == 0: return True
  l = len(nodeList)
  h = int(l/2) + 1
  for i in range(h):
    j = l - i - 1
    if nodeList[i].value != nodeList[j].value or len(nodeList[i].children) != len(nodeList[j].children):
      return False
  
  childrenList = []
  for node in nodeList:
    childrenList += node.children
  return helper(childrenList)
    
  

def is_symmetric(root):
  return helper([root])

tree = Node(4)
tree.children = [Node(3), Node(3)]
tree.children[0].children = [Node(9), Node(4), Node(1)]
tree.children[1].children = [Node(1), Node(4), Node(9)]
print (is_symmetric(tree))
# True