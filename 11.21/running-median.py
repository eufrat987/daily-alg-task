# Hi, here's your problem today. This problem was recently asked by Google:

# You are given a stream of numbers. 
# Compute the median for each new element .

# Eg. Given [2, 1, 4, 7, 2, 0, 5], the algorithm 
# should output [2, 1.5, 2, 3.0, 2, 2, 2]

# Here's a starting point:

def maxi(x,y): return x<y
def mini(x,y): return x>y

def makeHeap(arr, idx, l, comp):
    if idx is None: return
  
    midx = None
    if idx*2+1 < l: 
        midx = idx*2+1
    if idx*2+2 < l: 
        if comp(arr[midx], arr[idx*2+2]):
            midx = idx*2+2

    if midx is not None and comp(arr[idx], arr[midx]):
        arr[idx], arr[midx] = arr[midx], arr[idx]
    makeHeap(arr, midx, l, comp)

def addElement(v, l, m, r):
    if len(m) == 0: 
        m.append(v)
        return l, m, r
    
    if len(m) == 1:
        nm = None
        if v < m[0]: 
            l = [v] + l
            makeHeap(l,0,len(l),maxi)
            nm = l[0]
            l = l[1:]
        else: 
            r = [v] + r
            makeHeap(r,0,len(r),mini)
            nm = r[0]
            r = r[1:]
    
        if len(l) == len(r):
            if nm < m[0]:
                m = [nm] + m 
                m
            else: m = m + [nm]
        elif nm < m[0]:
            nm , m = m[0], [nm]
            l = [nm] + l
            makeHeap(l,0,len(l),maxi)
        else: 
            nm , m = m[0], [nm]
            r = [v] + r
            makeHeap(r,0,len(r),mini)

        return l, m, r
    
    if len(m) == 2:
        rm = None
        if v < m[0]:
            rm = m[1]
            m = [m[0]]
            l = [rm] + l
            r = [v] + r
        elif m[0] <= v and v < m[1]:
            rm1 = m[0]
            rm2 = m[1]
            m = [v]

            l = [rm1] + l
            r = [rm2] + r
        else: 
            rm = m[0]
            m = [m[1]]
            r = [v] + r
            l = [rm] + l
        
    makeHeap(l,0,len(l),maxi)
    makeHeap(r,0,len(r),mini)

    return l, m, r

def running_median(stream):
    l = []
    m = []
    r = []
    res = []

    for s in stream:
        l, m, r = addElement(s, l, m, r)
        if len(m) == 2:
            res.append(float(m[0]+m[1])/2)
        else: 
            res.append(m[0])
    
    return res

print(running_median([2, 1, 4, 7, 2, 0, 5]))
# 2 1.5 2 3.0 2 2.0 2