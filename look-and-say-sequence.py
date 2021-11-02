# Hi, here's your problem today. This problem was recently asked by Google:

# A look-and-say sequence is defined as the integer sequence beginning with a single digit 
# in which the next term is obtained by describing the previous term. An example is easier to understand:

# Each consecutive value describes the prior value.

# 1      #
# 11     # one 1's
# 21     # two 1's
# 1211   # one 2, and one 1.
# 111221 # #one 1, one 2, and two 1's.

# Your task is, return the nth term of this sequence.

class Solution:
    def term(self, nth):
        if nth==1: return '1'
        else:
            newTerm = ''
            prevTerm = self.term(nth-1)

            prevt = prevTerm[0]
            tc = 0
            for t in prevTerm:
                if prevt == t: tc+=1
                else: newTerm += str(tc)+prevt
                prevt = t

            newTerm += str(tc)+prevt
            
            return newTerm

                
for i in range(1,6):
    print (Solution().term(i))
# 1    
# 11     
# 21     
# 1211   
# 111221