# Hi, here's your problem today. This problem was recently asked by Microsoft:

# You are given an array of integers. Return the length of the longest 
# increasing subsequence (not necessarily contiguous) in the array.

# Example:
# [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

# The following input should return 6 since the longest increasing 
# subsequence is 0, 2, 6, 9 , 11, 15.

class Solution(object):
    def getIdxs(self, arr):
        sidxs = []
        m = min(arr)
        lm = None

        for i in range(len(arr)):
            n = arr[i]
            if lm is None:
                lm = n
                sidxs.append(i)
            elif n < lm:
                lm = n
                sidxs.append(i)
            if n == m: break

        return sidxs

    def calc(self, nums):
        if len(nums) == 0: return []

        sidxs = self.getIdxs(nums)
     
        maxx = None
        ret = []
        for idx in sidxs:
            l = nums[idx]

            new_nums = [i for i in nums[idx+1:] if i > l]

            sol = [l] + self.calc(new_nums)
    
            if maxx is None or maxx < len(sol):
                maxx = len(sol)
                ret = sol
        
        return ret
    
    def maxSubsequent(self, list):
        return len(self.calc(list))
        

print (Solution().maxSubsequent([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
# 6