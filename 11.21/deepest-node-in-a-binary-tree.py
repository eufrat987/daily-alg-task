# Hi, here's your problem today. This problem was recently asked by Google:

# You are given the root of a binary tree. Return the deepest node (the furthest node from the root).

# Example:

#     a
#   / \
#   b   c
#  /
# d

# The deepest node in this tree is d at depth 3.

# Here's a starting point:

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __repr__(self):
    # string representation
    return self.val

def deepest(node, lvl=1):
  lres, rres = None, None
  if node.left: 
      lres = deepest(node.left, lvl+1)
  if node.right:
      rres = deepest(node.right, lvl+1)
      
  if lres and rres:
      _, ll = lres
      _, rl = rres
      if ll > rl:
          return lres
      else: return rres
  if lres: return lres
  if rres: return rres
  
  return node,lvl

root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print (deepest(root))
# (d, 3)
