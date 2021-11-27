# Hi, here's your problem today. This problem was recently asked by Twitter:

# Given a list of integers, return the bounds of the minimum range that 
# must be sorted so that the whole list would be sorted.

# Example:
# Input: [1, 7, 9, 5, 7, 8, 10]
# Output: (1, 5)
# Explanation:
# The numbers between index 1 and 5 are out of order and need to be sorted.

# Here's your starting point:

def findRange(nums):
    m = min(nums)
    M = max(nums)
    arr = [0 for _ in range(0,M-m+1)]
    newNums = [0 for _ in nums]

    for n in nums:
        arr[n-m] += 1

    sum = 0
    for i in range(len(arr)):
        arr[i] = sum + arr[i]
        sum = arr[i]
    
    newNums[0] = m
    prev = arr[0]
    for i,v in enumerate(arr):
        if v == prev: 
            continue

        mv = v
        for _ in range(v-prev):
            newNums[mv-m] = i + m
            mv -= 1

    r = []
    for i in range(len(nums)):
        if len(r) == 0 and nums[i] != newNums[i]:
            r.append(i)
        elif len(r) == 1 and nums[i] == newNums[i]:
            r.append(i-1)
            break
    return r

  

print (findRange([1, 7, 9, 5, 7, 8, 10]))
# (1, 5)