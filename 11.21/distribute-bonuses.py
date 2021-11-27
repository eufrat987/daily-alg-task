# Hi, here's your problem today. This problem was recently asked by Twitter:

# You are the manager of a number of employees who all sit in a row. 
# The CEO would like to give bonuses to all of your employees, but since the company 
# did not perform so well this year the CEO would like to keep the bonuses to a minimum.

# The rules of giving bonuses is that:
# - Each employee begins with a bonus factor of 1x.
# - For each employee, if they perform better than the person sitting next to them, 
# the employee is given +1 higher bonus (and up to +2 if they perform better than both people to their sides).

# Given a list of employee's performance, find the bonuses each employee should get.

# Example:
# Input: [1, 2, 3, 2, 3, 5, 1]
# Output: [1, 2, 3, 1, 2, 3, 1]
# Here's your starting point:
def getScore(idx, performance):
    lidx, ridx = idx-1, idx+1
    score = 0
    if lidx >= 0 and performance[lidx] < performance[idx]:
        score += 1
    if ridx < len(performance) and performance[ridx] < performance[idx]:
        score += 1
    return score

def getBonuses(performance):
    res = [1 for _ in performance]
    for idx, p in enumerate(performance):
        v = getScore(idx,performance)
        res[idx] += v
    return res

print (getBonuses([1, 2, 3, 2, 3, 5, 1]))
# [1, 2, 3, 1, 2, 3, 1]