# Hi, here's your problem today. This problem was recently asked by AirBNB:

# Given a list of words, group the words that are anagrams of each other. 
# (An anagram are words made up of the same letters).

# Example:

# Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
# Output: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]

# Here's a starting point:

import collections



def groupAnagramWords(strs):
    d = collections.defaultdict(list)
    for word in strs:
        letters = collections.Counter(word)
        k = tuple(sorted(letters.items()))
        d[k].append(word)
    
    res = []
    for k in d.keys():
        res += [d[k]]

    return res

print (groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]