# Hi, here's your problem today. This problem was recently asked by Google:

# You are given an array of tuples (start, end) 
# representing time intervals for lectures. 
# The intervals may be overlapping. 
# Return the number of rooms that are required.

# For example. [(30, 75), (0, 50), (60, 150)] should return 2.

def merge(x1, y1, x2, y2):
    nx, ny = None, None
    if x1 > x2: 
        x1, x2 = x2, x1
        y1, y2 = y2, y1 
        
    if x1 < x2 and x2 < y1:
        nx = x2
        ny = min(y1,y2)
    return nx, ny

def roomSchedule(arr):
    workspace = []
    newWorkspace = arr.copy()

    rooms = 0
    while len(newWorkspace) > 0:
        workspace = newWorkspace
        newWorkspace = []
        rooms += 1

        for i in range(0, len(workspace)-1):
            for j in range(i, len(workspace)):
                x1, y1 = workspace[i]
                x2, y2 = workspace[j]
                
                nx, ny = merge(x1, y1, x2, y2)
                if nx is not None and ny is not None:
                    newWorkspace.append((nx, ny))

    return rooms

print(roomSchedule([(30, 75), (0, 50), (60, 150)]))
#2
