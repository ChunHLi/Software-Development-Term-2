def union(x,y):
    return intersection(x,y) + symmetricDifference(x,y)

def intersection(x,y):
    return [z for z in x if z in y]

def setDifference(x,y):
    return [z for z in x if z not in y]

def symmetricDifference(x,y):
    return setDifference(x,y) + setDifference(y,x)
    
def cartesianProduct(x,y):
    return [(a,z) for a in x for z in y]
