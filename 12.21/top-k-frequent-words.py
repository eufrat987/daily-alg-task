# Hi, here's your problem today. This problem was recently asked by AirBNB:

# Given a non-empty list of words, return the k most frequent words. 
# The output should be sorted from highest to lowest frequency, and 
# if two words have the same frequency, the word with lower alphabetical 
# order comes first. Input will contain only lower-case letters.

# Example:
# Input: ["daily", "interview", "pro", "pro", 
# "for", "daily", "pro", "problems"], k = 2
# Output: ["pro", "daily"]

class Solution(object):
  def topKFrequent(self, words, k):
      d = {}
      for ke in words:
        if ke not in d.keys(): d[ke] = 0
        d[ke] += 1

      r = []
      for ke in d.keys():
        if d[ke] >= k: r.append(ke)

      r.sort(key= lambda x: -d[x])
      return r

words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(Solution().topKFrequent(words, k))
# ['pro', 'daily']