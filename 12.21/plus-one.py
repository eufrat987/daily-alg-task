# Hi, here's your problem today. This problem was recently asked by LinkedIn:

# Given a non-empty array where each element represents a digit 
# of a non-negative integer, add one to the integer. The most significant 
# digit is at the front of the array and each element in the array contains only one digit. 
# Furthermore, the integer does not have leading zeros, except in the case of the number '0'.

# Example:
# Input: [2,3,4]
# Output: [2,3,5]

class Solution():
  def plusOne(self, digits, l):
      if l<0: Exception('Array to small')
      s = digits[l] + 1
      if s < 10: 
        digits[l] = s
        return digits
      else: 
        digits[l] = 0
        return self.plusOne(digits,l-1)
        

num = [2, 9, 9]
print(Solution().plusOne(num, len(num)-1))
# [3, 0, 0]