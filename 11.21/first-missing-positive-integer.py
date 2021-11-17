# Hi, here's your problem today. This problem was recently asked by Facebook:

# You are given an array of integers. Return the smallest positive integer 
# that is not present in the array. 
# The array may contain duplicate entries.

# For example, the input [3, 4, -1, 1] should return 2 because 
# it is the smallest positive integer 
# that doesn't exist in the array.

# Your solution should run in linear time and use constant space.

# Here's your starting point:

def first_missing_positive(nums):
    minv = None
    for n in nums:
        if minv is None or n > 0 and n < minv:
            minv = n
    if minv > 1: return 1

    i = 0
    while i < len(nums):
        n = nums[i]
        if n < len(nums) and n > 0:
            nn = nums[n-1]
            nums[n-1], nums[i] = n, nn

        n = nums[i]
        if n >= len(nums) or n <= 0 or n == i+1:
            i += 1
        elif n-1 >= 0 and n-1 < len(nums):
            nn = nums[n-1]
            if n == nn:
                i += 1

    for i,n in enumerate(nums):
        if n != i+1: return i+1

    return len(nums) + 1

        

print (first_missing_positive([3, 4, -1, 1]))
# 2