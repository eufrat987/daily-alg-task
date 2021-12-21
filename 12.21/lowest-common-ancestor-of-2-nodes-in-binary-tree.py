# Hi, here's your problem today. This problem was recently asked by Apple:

# You are given the root of a binary tree, along with two nodes, 
# A and B. Find and return the lowest common ancestor of A and B. 
# For this problem, you can assume that each node also has a pointer to its parent, 
# along with its left and right child.

class TreeNode:
  def __init__(self, val):
    self.left = None
    self.right = None
    self.parent = None
    self.val = val


def nodeLvl(root, node, lvl = 0):
  if root == node: return lvl
  if root is None: return None
  r = nodeLvl(root.left, node, lvl+1)
  if r is not None: return r
  r = nodeLvl(root.right, node, lvl+1)
  if r is not None: return r

def lowestCommonAncestor(root, a, b):
    alvl = nodeLvl(root, a)
    blvl = nodeLvl(root, b)
    while alvl != blvl:
      if alvl < blvl:
        b = b.parent
        blvl -= 1
      else: 
        a = a.parent
        alvl -= 1
    while a != b: 
      a = a.parent
      b = b.parent
    return a

#   a
#  / \
# b   c
#    / \
#   d*  e*
root = TreeNode('a')
root.left = TreeNode('b')
root.left.parent = root
root.right = TreeNode('c')
root.right.parent = root
a = root.right.left = TreeNode('d')
root.right.left.parent = root.right
b = root.right.right = TreeNode('e')
root.right.right.parent = root.right

print (lowestCommonAncestor(root, a, b).val)
# c