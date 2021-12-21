# Hi, here's your problem today. This problem was recently asked by Microsoft:

# Given the root of a binary tree, print its level-order traversal. For example:

#   1
#  / \
# 2   3
#    / \
#   4   5

# The following tree should output 1, 2, 3, 4, 5.

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def print_level_order(root, toPrint = []):
  if len(toPrint) == 0 and root is not None: 
    print_level_order(None, [root])
    return
  elif len(toPrint) == 0: return
  c = toPrint.pop()
  print(c.val)
  if c.left is not None: toPrint = [c.left] + toPrint
  if c.right is not None: toPrint = [c.right] + toPrint
  print_level_order(root, toPrint)

root = Node(1, Node(2), Node(3, Node(4), Node(5)))
print_level_order(root)
# 1 2 3 4 5