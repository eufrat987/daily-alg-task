# Hi, here's your problem today. This problem was recently asked by Uber:

# You have a landscape, in which puddles can form. 
# You are given an array of non-negative integers representing the elevation at each location. 
# Return the amount of water that would accumulate if it rains.

# For example: [0,1,0,2,1,0,1,3,2,1,2,1] should return 6 because 6 units of water can get trapped here.
#        X               
#    X███XX█X              
#  X█XX█XXXXXX                   
# [0,1,0,2,1,0,1,3,2,1,2,1]
# Here's your starting pont:

def capacity(arr):
    mil, mir = [], []
    for i in range(len(arr)):
        if len(mil) > 0:
            mil.append(max(mil[-1], arr[i]))
        else: mil.append(arr[i])

        ridx = len(arr) - i - 1
        if len(mir) > 0:
            mir.append(max(mir[-1], arr[ridx]))
        else: mir.append(arr[ridx])
    mir.reverse()

    res = []
    for i in range(len(arr)):
        res.append(min(mil[i],mir[i]) - arr[i])

    return sum(res)


print (capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6