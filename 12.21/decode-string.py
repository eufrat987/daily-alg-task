# Hi, here's your problem today. This problem was recently asked by Google:

# Given a string with a certain rule: k[string] 
# should be expanded to string k times. So for example, 
# 3[abc] should be expanded to abcabcabc. Nested expansions can happen, 
# so 2[a2[b]c] should be expanded to abbcabbc.

# Your starting point:

def getStr(s):
    ii,jj = 0,0
    for i,c in enumerate(s):
        if c=='[': 
            ii=i
            break
    for i in range(len(s)-1, -1, -1):
        c = s[i]
        if c==']': 
            jj=i
            break
    return s[ii+1:jj], s[jj+1:]

def decodeString(s):
    res = ''
    for i, c in enumerate(s):
        try:
            v = int(c)
            ls,rs = getStr(s)
            ds = decodeString(ls)
            for i in range(v):
                res += ds
            return res + decodeString(rs)
        except:
            res += c
    return res

print (decodeString('2[a2[b]c]'))
# abbcabbc