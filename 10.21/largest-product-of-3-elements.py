# Hi, here's your problem today. This problem was recently asked by Microsoft:

# You are given an array of integers. Return the largest product that can be made by multiplying any 3 integers in the array.

# Example:

# [-4, -4, 2, 8] should return 128 as the largest product can be made by multiplying -4 * -4 * 8 = 128.

# Here's a starting point:

import functools
import operator



def split(nums, ks, kns):
    s, us = [], []
    for n in nums:
        if n>=0: 
            if len(s) == ks:
                min_s = min(s)
                if n>min_s:
                    s.append(n)
                    s.sort()
                    s.reverse()
                    s = s[:ks]
            else: 
                s.append(n)
                s.sort()
                s = s[:ks]
        else:
            if len(us) == kns:
                max_us = max(us)
                if n<max_us:
                    us.append(n)
                    us.sort()
                    us = us[:kns]
            else: 
                us.append(n)
                us.sort()
                us.reverse()
                us = us[:kns]
    s.reverse()
        
    return s, us


def maximum_product_of_three(lst):
    config = [  
        {'+': 3, '-': 0}, 
        {'+': 1, '-': 2} 
    ]

    maxs = max(config, key=lambda x: x['+'])['+']
    maxus = max(config, key=lambda x: x['-'])['-']

    s, us = split(lst, maxs, maxus)

    res = []

    for c in config:
        pluses = c['+']
        minuses = c['-']

        plusNums = s[:pluses]
        minusNums = us[:minuses]

        x = functools.reduce(operator.mul, plusNums + minusNums)
        res.append(x)


  
    return max(res)
    # for config in ['+++', '+--']:

print (maximum_product_of_three([-4, -4, 2, 8]))
# 128