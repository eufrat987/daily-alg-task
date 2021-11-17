# Hi, here's your problem today. This problem was recently asked by Google:

# You are given a hash table where the key is a course code, and the value is a list of all the course codes that are prerequisites for the key. Return a valid ordering in which we can complete the courses. If no such ordering exists, return NULL.

# Example:
# {
#   'CSC300': ['CSC100', 'CSC200'], 
#   'CSC200': ['CSC100'], 
#   'CSC100': []
# }

# This input should return the order that we need to take these courses:
#  ['CSC100', 'CSC200', 'CSCS300']

# Here's your starting point:

def courses_to_take(course_to_prereqs):
    result = []
    r = True
    while r:
        r = False
        for k in course_to_prereqs.keys():
            if course_to_prereqs[k] == []:
                r = True
                result.append(k)
                for kk in course_to_prereqs:
                    course_to_prereqs[kk] = [v for v in course_to_prereqs[kk] if v != k]
        if r:
            added = result[-1]
            del course_to_prereqs[added]

    if result == []: return None
    return result


courses = {
  'CSC300': ['CSC100', 'CSC200'], 
  'CSC200': ['CSC100'], 
  'CSC100': []
}

print (courses_to_take(courses))
# ['CSC100', 'CSC200', 'CSC300']