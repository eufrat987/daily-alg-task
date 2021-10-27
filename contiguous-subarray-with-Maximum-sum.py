# Hi, here's your problem today. This problem was recently asked by Twitter:

# You are given an array of integers. Find the maximum sum of all possible contiguous subarrays of the array.

# Example:

# [34, -50, 42, 14, -5, 86]
 
# Given this input array, the output should be 137. The contiguous subarray with the largest sum is [42, 14, -5, 86].

# Your solution should run in linear time.

# Here's a starting point:

def max_subarray_sum(arr):
    intervals = []
    idx = 0
    
    added = 0
    sum = 0
    sumidx = []
    
    while added != len(arr):

        sum = 0
        sumidx = []
        while idx<len(arr) and arr[idx]>=0 :
            added+=1
            sum += arr[idx]
            sumidx.append(idx)
            idx+=1
            
        intervals.append((sum, sumidx))

        sum = 0
        sumidx = []
        
        if not idx<len(arr): break

        while idx<len(arr) and arr[idx]<0:
            added+=1
            sum+=arr[idx]
            sumidx.append(idx)
            idx+=1
            
        intervals.append((sum, sumidx))
    
    v, _ = intervals[0]
    if v < 0: intervals = [(0,[])] + intervals
    v, _ = intervals[-1]
    if v < 0: intervals = intervals + [(0,[])]
    
    res = helper(intervals)
    v,_ = res[0]

    return v

def getlS(intervals, idx):
    v, idx1 = intervals[idx-1]
    v2, idx2 = intervals[idx] 
    return (v+v2, idx1+idx2) 

def getrS(intervals, idx):
    v2, idx2 = intervals[idx] 
    v3, idx3 = intervals[idx+1]
    return (v2+v3, idx2+idx3) 

def getS(intervals, idx):
    v2, idx2 = getlS(intervals, idx)
    v3, idx3 = intervals[idx+1]
    return (v2+v3, idx2+idx3) 

def helper(intervals):
    idx = 0
    delLeft = True

    while len(intervals) > 1:
        if delLeft:
            idx = 1
        else:
            idx = len(intervals) - 2

        vf, idxsf = getS(intervals, idx)

        if delLeft:
            vl, _ = getlS(intervals, idx)
            if vl<0: 
                intervals = intervals[idx+1:]
            else: 
                vf, idxsf = getS(intervals,idx)
                intervals = intervals[idx+1:]
                intervals[idx-1] = (vf, idxsf)

            delLeft = False
            continue
        else: 
            vr, _ = getrS(intervals, idx)
            if vr<0: 
                intervals = intervals[:idx-1]
            else: 
                vf, idxsf = getS(intervals,idx)
                intervals = intervals[:idx]
                intervals[idx-1] = (vf, idxsf)
                
            delLeft = True
            continue

    return intervals


  
print (max_subarray_sum([34, -50, 42, 14, -5, 86]))
# 137