# Hi, here's your problem today. This problem was recently asked by Amazon:

# You are given an array of integers. Return the length of the longest 
# consecutive elements sequence in the array.

# For example, the input array [100, 4, 200, 1, 3, 2] has the longest
#  consecutive sequence 1, 2, 3, 4, 
# and thus, you should return its length, 4.

def longest_consecutive(nums):
    nums.sort()
    res = []
    tmp = []
    for n in nums:
        if len(tmp) == 0: tmp.append(n)
        elif tmp[-1]+1 == n: tmp.append(n)
        else: 
            res.append(tmp)
            tmp = []
    ml = None
    for r in res:
        if ml is None or len(r) > ml: ml = len(r)
    
    return ml

print (longest_consecutive([100, 4, 200, 1, 3, 2]))
# 4