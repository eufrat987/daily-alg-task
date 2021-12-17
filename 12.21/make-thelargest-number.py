# Hi, here's your problem today. This problem was recently asked by Uber:

# Given a number of integers, combine them so it would create the largest number.

# Example:
# Input:  [17, 7, 2, 45, 72]
# Output:  77245217

from functools import cmp_to_key

def compare(x, y):
    sx = int(str(x)[0])
    sy = int(str(y)[0])
    lx = len(str(x))
    ly = len(str(y))
    if x==y: return lx - ly
    return sy - sx

def largestNum(nums):
    nums = sorted(nums, key=cmp_to_key(compare))
    r = ''
    for n in nums:
        r+=str(n) 
    return r

print (largestNum([17, 7, 2, 45, 72]))
# 77245217