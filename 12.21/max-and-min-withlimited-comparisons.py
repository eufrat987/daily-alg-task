# Hi, here's your problem today. This problem was recently asked by Microsoft:

# Given a list of numbers of size n, where n is greater than 3, 
# find the maximum and minimum of the list using less than 2 * (n - 1) comparisons.

# Here's a start:

<<<<<<< HEAD
def find_min_max(nums):
    pass
=======
def minMax(ar, ar2):
    m = min(ar[0],ar2[0])
    M = max(ar[1],ar2[1])
    return [m,M]

def find_min_max(nums):
    if len(nums) > 2: 
        l = int(len(nums) / 2)
        arr = find_min_max(nums[:l])
        arr2= find_min_max(nums[l:])

        m, M = arr[0], arr[0]
        if len(arr) == 2:
            M = arr[1]

        m2, M2 = arr2[0], arr2[0]
        if len(arr2) == 2:
            M2 = arr2[1]
            
        return [min(m,m2),max(M, M2)]

    if len(nums) == 2: 
        if nums[0] > nums[1]: 
            nums[0], nums[1] = nums[1], nums[0]
        return nums

    else: return nums
>>>>>>> 167b860 (max-and-min-withlimited-comparisons)

print (find_min_max([3, 5, 1, 2, 4, 8]))
# (1, 8)
