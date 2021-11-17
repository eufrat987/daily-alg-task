# Hi, here's your problem today. This problem was recently asked by Facebook:

# Given a list, find the k-th largest element in the list.
# Input: list = [3, 5, 2, 4, 6, 8], k = 3
# Output: 5
# Here is a starting point:

class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.leftArr = []
        self.right = None
        self.rightArr = []
    def add(self, val):
        if val < self.val:
            self.leftArr.append(val)
            if self.left: self.leftArr.add(val)
            else: self.left = Node(val)
        else: 
            self.rightArr.append(val)
            if self.right: self.right.add(val)
            else: self.right = Node(val)
    def p(self):
        print(self.val, self.leftArr, self.rightArr)
        if self.left: self.left.p()
        if self.right: self.right.p()
    
    def kth(self, k, parent_k = 0):
        eval = (len(self.rightArr) + 1) + parent_k
        if k == eval: return self.val
        else: 
            if k > eval: return self.left.kth(k,eval)
            else: return self.right.kth(k,0) 

def findKthLargest(nums, k):
    s = len(nums)
    r = Node(nums[0])
    
    for n in nums[1:]:
        r.add(n)

    return r.kth(k)
   


print (findKthLargest([3, 5, 2, 4, 6, 8], 3))
# 5

