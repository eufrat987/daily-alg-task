# Hi, here's your problem today. This problem was recently asked by Facebook:

# Two words can be 'chained' if the last character of the first 
# word is the same as the first character of the second word.

# Given a list of words, determine if there is a way to 'chain' 
# all the words in a circle.

# Example:
# Input: ['eggs', 'karat', 'apple', 'snack', 'tuna']
# Output: True
# Explanation:
# The words in the order of 
# ['apple', 'eggs', 'snack', 'karat', 'tuna'] creates a circle of chained words.

# Here's a start:

from collections import defaultdict

def chainedWords(words):
    d = {}
    for w in words:
        assert (w[0] not in d.keys()), 'Not handled case!'
        d[w[0]] = w
    
    next = words.pop()
    try:
        while(len(words)) > 0:
            next = d[next[-1]]
            words.remove(next)
    except: return False

    return True

print (chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna']))
# True