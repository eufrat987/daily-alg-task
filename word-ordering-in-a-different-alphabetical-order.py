# Hi, here's your problem today. This problem was recently asked by Apple:

# Given a list of words, and an arbitrary alphabetical order, 
# verify that the words are in order of the alphabetical order.

# Example:
# Input:
# words = ["abcd", "efgh"], order="zyxwvutsrqponmlkjihgfedcba"

# Output: False
# Explanation: 'e' comes before 'a' so 'efgh' should come before 'abcd'

# Example 2:
# Input:
# words = ["zyx", "zyxw", "zyxwy"],
# order="zyxwvutsrqponmlkjihgfedcba"

# Output: True
# Explanation: The words are in increasing alphabetical order

# Here's a starting point:

def compare(w1, w2, od):
    lll = min(len(w1), len(w2))
    i = 0
    while i < lll and w1[i] == w2[i]: i+=1
    if i == lll: return True
    if w1[i] in od[w2[i]]: return False
    return True

def isSorted(words, order):
    d = {}
    r = True
    for i in range(len(order)):
        k = order[i]
        for j in range(i+1,len(order)):
            v = order[j]
            if k not in d.keys(): d[k] = []
            d[k] += [v]
    for i in range(len(words)-1):
        w1 = words[i]
        w2 = words[i+1]
        r &= compare(w1, w2,d)

    return r

print (isSorted(["abcd", "efgh"], 
                "zyxwvutsrqponmlkjihgfedcba"))
# False
print (isSorted(["zyx", "zyxw", "zyxwy"],
               "zyxwvutsrqponmlkjihgfedcba"))
# True
