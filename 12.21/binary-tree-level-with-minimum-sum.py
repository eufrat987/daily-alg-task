# Hi, here's your problem today. This problem was recently asked by Twitter:

# You are given the root of a binary tree. Find the level for the binary tree with the minimum sum, 
# and return that value.

# For instance, in the example below, the sums of the trees are 10, 2 + 8 = 10, and 4 + 1 + 2 = 7. 
# So, the answer here should be 7.

class Node:
  def __init__(self, value, left=None, right=None):
    self.val = value
    self.left = left
    self.right = right

def helper(arr, mini = None):
    if len(arr) == 0: return mini
    val = 0
    newArr = []
    for a in arr:
        val += a.val
        if a.left is not None:
            newArr.append(a.left)
        if a.right is not None:
            newArr.append(a.right)
    if mini is not None:
        newMin = min(val, mini)
        return helper(newArr, newMin)
    else:
        return helper(newArr, val)

def minimum_level_sum(root):
    return helper([root])
    

#     10
#    /  \
#   2    8
#  / \    \
# 4   1    2
node = Node(10)
node.left = Node(2)
node.right = Node(8)
node.left.left = Node(4)
node.left.right = Node(1)
node.right.right = Node(2)

print (minimum_level_sum(node))