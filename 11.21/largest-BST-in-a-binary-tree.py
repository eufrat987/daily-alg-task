# Hi, here's your problem today. This problem was recently asked by Twitter:

# You are given the root of a binary tree. Find and return 
# the largest subtree of that tree, which is a valid binary search tree.

# Here's a starting point:

class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

  def __str__(self):
    # preorder traversal
    answer = str(self.key)
    if self.left:
      answer += str(self.left)
    if self.right:
      answer += str(self.right)
    return answer

def largest_bst_subtree(root):
    if not root: return None
    if root.left and root.right and root.left.key < root.key and root.right.key >= root.key: 
        return root
    else: 
        l = largest_bst_subtree(root.left)
        r = largest_bst_subtree(root.right)
        if l and r:
            if len(str(l)) > len(str(r)):
                return l
            else: return r
        elif l: return l
        elif r: return r

#     5
#    / \
#   6   7
#  /   / \
# 2   4   9
node = TreeNode(5)
node.left = TreeNode(6)
node.right = TreeNode(7)
node.left.left = TreeNode(2)
node.right.left = TreeNode(4)
node.right.right = TreeNode(9)
print (largest_bst_subtree(node))
#749