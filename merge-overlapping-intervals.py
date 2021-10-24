# Hi, here's your problem today. This problem was recently asked by Microsoft:

# You are given an array of intervals - that is, an array of tuples (start, end). The array may not be sorted, 
# and could contain overlapping intervals. Return another array where the overlapping intervals are merged.

# For example:
# [(1, 3), (5, 8), (4, 10), (20, 25)]

# This input should return [(1, 3), (4, 10), (20, 25)] since (5, 8) and (4, 10) can be merged into (4, 10).

# Here's a starting point:

def merge(intervals):
    resx = []
    resy = []

    for x, y in intervals:
        replaced = False
        for i in range(len(resx)):
            xx = resx[i]
            yy = resy[i]
            if x < xx and y < yy and xx < y or \
                xx<x and yy<y and x<yy or \
                    x<xx and yy<y or \
                        xx<y and y<yy:
                        resx[i] = min(x,xx)
                        resy[i] = max(y,yy)
                        replaced = True
                        break
        if not replaced:
            resx.append(x)
            resy.append(y)

    res = []

    for i in range(len(resx)):
        res.append((resx[i], resy[i]))

    return res
    

          
      
  
print (merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
# [(1, 3), (4, 10), (20, 25)]