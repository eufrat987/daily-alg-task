# Hi, here's your problem today. This problem was recently asked by Facebook:

# You are given an array of integers. Return all the permutations of this array.

def helper(nums, arr):
    if len(arr) == len(nums): return [arr]
    res = []
    for n in nums:
        if n in arr: continue
        res += helper(nums, arr + [n])
    return res

def permute(nums):
    return helper(nums, [])

print (permute([1, 2, 3]))
# [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]