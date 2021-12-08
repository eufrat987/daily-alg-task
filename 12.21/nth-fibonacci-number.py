# Hi, here's your problem today. This problem was recently asked by Apple:

# The Fibonacci sequence is the integer sequence defined by the recurrence relation: 
# F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1. In other words, 
# the nth Fibonacci number is the sum of the prior two Fibonacci numbers. 
# Below are the first few values of the sequence:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...

# Given a number n, print the n-th Fibonacci Number.
# Examples:
# Input: n = 3
# Output: 2

# Input: n = 7
# Output: 13
# Here's a starting point:

class Solution():
  def getArr(self, n, arr):
      if len(arr) == n+1: return arr
      else:
        v = arr[-1] + arr[-2]
        return self.getArr(n, arr + [v])

  def fibonacci(self, n):
      return self.getArr(n, [0,1])[-1]

n = 9
print(Solution().fibonacci(n))
# 34