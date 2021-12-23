# Hi, here's your problem today. This problem was recently asked by Twitter:

# Given an array of integers of size n, where all elements 
# are between 1 and n inclusive, find all of the elements of [1, n] 
# that do not appear in the array. Some numbers may appear more than once.

# Example:
# Input: [4,5,2,6,8,2,1,5]
# Output: [3,7]

def make(nums, idx, n):
  if n-1 != idx and n != -1:
      if nums[idx] == nums[n-1]:
         nums[n-1] = n
         nums[idx] = -1
      nums[idx], nums[n-1] = nums[n-1], nums[idx]
      make(nums, idx, nums[idx])

class Solution(object):
  def findDisappearedNumbers(self, nums):
      for idx, n in enumerate(nums):
        make(nums, idx, n)
      res = []
      for idx, n in enumerate(nums):
        if n==-1: res.append(idx+1)
      return res

nums = [4, 6, 2, 6, 7, 2, 1]
print(Solution().findDisappearedNumbers(nums))
# [3, 5]