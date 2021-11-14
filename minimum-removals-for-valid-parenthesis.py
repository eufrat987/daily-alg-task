# Hi, here's your problem today. This problem was recently asked by Uber:

# You are given a string of parenthesis. Return 
# the minimum number of parenthesis that would need to be removed 
# in order to make the string valid. "Valid" means that 
# each open parenthesis has a matching closed parenthesis.

# Example:

# "()())()"

# The following input should return 1.

# ")("

# Here's a start:

def count_invalid_parenthesis(string):
    op ,cp = 0, 0
    rp = 0
    for s in string:
        if s == '(': op += 1
        elif s == ')' and op > cp: cp += 1
        else: rp += 1
    return op - cp + rp

print (count_invalid_parenthesis("()())()"))
# 1