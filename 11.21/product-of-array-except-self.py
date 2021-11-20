# Hi, here's your problem today. This problem was recently asked by Amazon:

# You are given an array of integers. 
# Return an array of the same size where 
# the element at each index is the product of all the elements 
# in the original array except for the element at that index.

# For example, an input of [1, 2, 3, 4, 5] 
# should return [120, 60, 40, 30, 24].

# You cannot use division in this problem.

# Here's a start:

def products(nums):
    res = [1 for _ in nums]
    
    for i in range(len(nums)):
        for j in [k for k in range(len(nums)) if k != i]:
            res[i] *= nums[j]

    return res

print (products([1, 2, 3, 4, 5]))
# [120, 60, 40, 30, 24]