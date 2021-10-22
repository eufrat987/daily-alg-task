# Hi, here's your problem today. This problem was recently asked by Amazon:

# You are given a 2D array of integers. Print out the clockwise spiral traversal of the matrix.

# Example:

# grid = [[1,  2,  3,  4,  5],
#         [6,  7,  8,  9,  10],
#         [11, 12, 13, 14, 15],
#         [16, 17, 18, 19, 20]]

# The clockwise spiral traversal of this array is:

# 1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12

# Here is a starting point:

def getMoment(momentum):
    if momentum == [0,1]:
        return [1,0]
    if momentum == [1,0]:
        return [0,-1]
    if momentum == [0, -1]:
        return [-1,0]
    if momentum == [-1,0]:
        return [0,1]

def matrix_spiral_print(M):
  
    momentum = [0,1]
    visited = []
    starting = [0,0]

    while len(visited) != len(M)*len(M[0]):
   
        p = M[starting[0]][starting[1]]
        visited.append(p)

        if len(visited) == len(M)*len(M[0]): break

        v = [starting[0] + momentum[0], starting[1] + momentum[1]]
        while v[0] >= len(M) or v[1] >= len(M[0]) or M[v[0]][v[1]] in visited:
            momentum = getMoment(momentum)
            v = [starting[0] + momentum[0], starting[1] + momentum[1]]
        
        starting = v

    print(visited)

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12