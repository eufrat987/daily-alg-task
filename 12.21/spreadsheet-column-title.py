# Hi, here's your problem today. This problem was recently asked by Amazon:

# MS Excel column titles have the following pattern: A, B, C, ..., 
# Z, AA, AB, ..., AZ, BA, BB, ..., ZZ, AAA, AAB, ... etc. 
# In other words, column 1 is named "A", column 2 is "B", column 26 is "Z", 
# column 27 is "AA" and so forth. Given a positive integer, find its corresponding column name.
# Examples:
# Input: 26
# Output: Z

# Input: 51
# Output: AY

# Input: 52
# Output: AZ

# Input: 676
# Output: YZ

# Input: 702
# Output: ZZ

# Input: 704
# Output: AAB
# Here is a starting point:

class Solution:
  def incL(self, res, idx):
      if idx < 0: 
          res = ['A'] + res
          return res

      if res[idx] == 'Z':
          res[idx] = 'A'
         
          res = self.incL(res, idx-1)
          return res

      res[idx] = chr(ord(res[idx])+1)
  
      return res

  def convertToTitle(self, n):
      i = 1
      res = ['A']

      while i < n:
          res = self.incL(res, len(res)-1)
          i+=1

      return ''.join(res)

input1 = 1
input2 = 456976
input3 = 28
print(Solution().convertToTitle(input1))
# A
print(Solution().convertToTitle(input2))
# YYYZ
print(Solution().convertToTitle(input3))
# AB
print(Solution().convertToTitle(702))