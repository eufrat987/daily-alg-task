# Hi, here's your problem today. This problem was recently asked by LinkedIn:

# Given a sorted list of numbers, change it into a balanced binary search tree. You can assume there will be no duplicate numbers in the list.

# Here's a starting point:

from collections import deque

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    # level-by-level pretty-printer
    nodes = deque([self])
    answer = ''
    while len(nodes):
      node = nodes.popleft()
      if not node:
        continue
      answer += str(node.value)
      nodes.append(node.left)
      nodes.append(node.right)
    return answer

def getlr(nums):
    m = int(len(nums) / 2) 
    return nums[:m], nums[m+1:]

def help(parent, nums):
    lnums, rnums = getlr(nums)

    llen = len(lnums)
    if llen > 0:
        l = int(llen / 2)
        parent.left = Node(lnums[l])
        help(parent.left, lnums)

    rlen = len(rnums)
    if rlen > 0:
        r = int(rlen / 2)
        parent.right = Node(rnums[r])
        help(parent.right, rnums)

def createBalancedBST(nums):
    x = int(len(nums) / 2)
    root = Node(nums[x])
    help(root, nums)

    return root

print (createBalancedBST([1, 2, 3, 4, 5, 6, 7, 8]))
# 4261357
#   4
#  / \
# 2   6
#/ \ / \
#1 3 5 7s
