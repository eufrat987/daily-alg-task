# Hi, here's your problem today. This problem was recently asked by Apple:

# Given an array of integers, arr, where all numbers 
# occur twice except one number which occurs once, 
# find the number. Your solution should 
# ideally be O(n) time and use constant extra space.

# Example:
# Input: arr = [7, 3, 5, 5, 4, 3, 4, 8, 8]
# Output: 7

class Solution(object):
  def findSingle(self, nums):
    if max(nums) >= len(nums) or min(nums) < 0: 
      raise Exception("Sorry, not supported case")
    for idx, n in enumerate(nums):
      if nums[n] == n and n != idx: 
        nums[n] = -1
        nums[idx] = -1
      elif n == idx: 
        nums[idx], nums[n] = nums[n], nums[idx]
    for n in nums:
      if n != -1: return n

nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
print(Solution().findSingle(nums))
# 3