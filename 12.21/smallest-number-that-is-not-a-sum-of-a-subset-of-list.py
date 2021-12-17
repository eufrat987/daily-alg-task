# Hi, here's your problem today. This problem was recently asked by AirBNB:

# Given a sorted list of positive numbers, 
# find the smallest positive number that cannot 
# be a sum of any subset in the list.

# Example:
# Input: [1, 2, 3, 8, 9, 10]
# Output: 7
# Numbers 1 to 6 can all be summed by a subset 
# of the list of numbers, but 7 cannot.

def check(arr, find):
    arr = [i for i in arr if i <= find]
    if len(arr) == 0: return find == 0
    a = arr[0]
    arr = arr[1:]
    return check(arr, find-a) or check(arr, find)

def findSmallest(nums):
    r = []
    prev = None
    for n in nums:
        if prev is not None and prev + 1 != n:
            for i in range(prev + 1, n):
                r.append(i)
        prev = n
    r.append(max(nums)+1)
    r.reverse()
    while True:
        c = r.pop()
        v = check(nums, c)
        if not v: return c
        if len(r) == 1: r = [r[0]+1] +  r

print (findSmallest([1, 2, 3, 8, 9, 10]))
# 7