# Hi, here's your problem today. This problem was recently asked by Amazon:

# You are given an array of integers, and an integer K. 
# Return the subarray which sums to K. 
# You can assume that a solution will always exist.

def find_continuous_k(list, k, visited = []):
    print(list)
    if k == 0: return visited
    if len(list) == 0: return None
    list = [i for i in list if i <= k]
    l = list[0]
    list = list[1:]
    r = find_continuous_k(list, k, visited)
    if r is not None: return r
    r = find_continuous_k(list, k-l, visited + [l])
    if r is not None: return r

print (find_continuous_k([1, 3, 2, 5, 7, 2], 14))
# [2, 5, 7]