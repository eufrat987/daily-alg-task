# Hi, here's your problem today. This problem was recently asked by LinkedIn:

# Given a string, rearrange the string so that no character next to each other are the same. 
# If no such arrangement is possible, then return None.

# Example:
# Input: abbccc
# Output: cbcbca

def rearrangeString(s):
    d = {}
    r = ''
    for c in s:
        if c not in d.keys(): d[c] = 0
        d[c] += 1
    l = list(d.keys())
    l.sort(key=lambda x: -d[x])
    while len(l) > 0:
        for c in l:
            if d[c] > 0: 
                d[c] -= 1
                if len(r)>0 and r[-1] == c: 
                    return None
                r += c
            if d[c] == 0: l.remove(c)
    return r


print (rearrangeString('abbccc'))
# cbcabc