# Hi, here's your problem today. This problem was recently asked by AirBNB:

# Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

# Example 1:
# Input: A = "ab", B = "ba"
# Output: true
# Example 2:

# Input: A = "ab", B = "ab"
# Output: false
# Example 3:
# Input: A = "aa", B = "aa"
# Output: true
# Example 4:
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
# Example 5:
# Input: A = "", B = "aa"
# Output: false
# Here's a starting point:

class Solution:
  def buddyStrings(self, A, B):
    la = len(A)
    if la != len(B): return False

    dch = []
    for i in range(la):
        if A[i] != B[i]: 
            dch += [A[i], B[i]]
    
    if len(dch) == 4:
        if dch[0] == dch[3]: return True

    return False

print (Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print (Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False