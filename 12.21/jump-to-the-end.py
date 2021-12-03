# Hi, here's your problem today. This problem was recently asked by Facebook:

# Starting at index 0, for an element n at index i, you are allowed 
# to jump at most n indexes ahead. Given a list of numbers, 
# find the minimum number of jumps to reach the end of the list.

# Example:
# Input: [3, 2, 5, 1, 1, 9, 3, 4]
# Output: 2
# Explanation:

# The minimum number of jumps to get to the end of the list is 2:
# 3 -> 5 -> 4

# Here's a starting point:

def jumpToEnd(nums):
    s = 0
    j = 0
    while j < len(nums):
        m = 0
        ii = 0
        for i, c in enumerate(nums[j:]):
            if m < i+c:
                m = i+c
                ii=i
        j += c
        s += 1
    return s


print (jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4]))
# 2