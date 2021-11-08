# Hi, here's your problem today. This problem was recently asked by Microsoft:

# You are given the preorder and inorder traversals of a binary tree 
# in the form of arrays. Write a function that reconstructs the tree 
# represented by these traversals.

# Example:
# Preorder: [a, b, d, e, c, f, g]
# Inorder: [d, b, e, a, f, c, g]

# The tree that should be constructed from these traversals is:

#     a
#    / \
#   b   c
#  / \ / \
# d  e f  g

# Here's a start:

from collections import deque

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __str__(self):
    q = deque()
    q.append(self)
    result = ''
    while len(q):
      n = q.popleft()
      result += n.val
      if n.left:
        q.append(n.left)
      if n.right:
        q.append(n.right)

    return result

def reconstruct(preorder, inorder):
    v = preorder[0]
    if len(preorder) == 1: return Node(v)

    vIdx = inorder.index(v)
    
    larr = inorder[:vIdx]
    rarr = []
    if vIdx+1 < len(inorder): 
        rarr = inorder[vIdx+1:]
    
    lpre = [i for i in preorder if i in larr]
    rpre = [i for i in preorder if i in rarr]

    root = Node(v)
    root.left = reconstruct(lpre, larr)
    root.right = reconstruct(rpre, rarr)
    return root

        

tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                   ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
print (tree)
# abcdefg