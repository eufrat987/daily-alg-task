# Hi, here's your problem today. This problem was recently asked by Facebook:

# Given a file path with folder names, '..' (Parent directory), and '.' (Current directory), 
# return the shortest possible file path (Eliminate all the '..' and '.').

# Example
# Input: '/Users/Joma/Documents/../Desktop/./../'
# Output: '/Users/Joma/'

def shortest_path(file_path):
    res = file_path.split('/')
    cres = []
    for idx, f in enumerate(res):
        if f == '': continue
        if f == '.': continue
        if f == '..': 
            cres.pop()
            continue
        cres.append(f)
    return '/' + '/'.join(cres)

print (shortest_path('/Users/Joma/Documents/../Desktop/./../'))
# /Users/Joma/