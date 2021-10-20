# Hi, here's your problem today. This problem was recently asked by Facebook:

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

# Here is a starting point:

class Solution:
  def moveZeros(self, nums):
    idx = -1
    for n in range(len(nums)): 
        if nums[n] == 0: 
            idx = n
            break
    if idx == -1: return 

    mz = False
    for n in range(len(nums)):
        if nums[n] == 0: mz = True
        if nums[n] != 0 and mz:
            mz = False 
            tmp = nums[n] 
            nums[n] = nums[idx]
            nums[idx] = tmp
            for i in range(idx, n):
                if nums[i] == 0:
                    idx = i
                    mz = True
                    break
            print(nums, idx)
        
            


nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
nums = [ 1,2,3,0,4]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]