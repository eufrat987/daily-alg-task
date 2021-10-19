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