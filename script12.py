
setA =  {11,22,33}
setB = {33,44,55}
setC  = setA.union(setB)
print(setC)

setD = {11,22,33}
setE = {11,55,33,77}


# setR = setD.intersection(setE)
# # print(setR)

# setD.intersection_update(setE)
# print(setD)

# setE.intersection_update(setD)
# print(setE)

# program 2

setG = {22,33,44}
setH = {33,88,99}

# setZ  = setG.difference(setH)
# print(setZ)

# setK = setH.difference(setG)
# print(setK)

# setH.difference_update(setG)
# print(setH)

setG.difference_update(setH)
print(setG)


# program 3

setQ = {44,55,66}
setL = {99,77,88,44}

# setY = setQ.symmetric_difference(setL)
# print(setY)

setQ.symmetric_difference_update(setL)
print(setQ)


setA = {11,22,33}
setB = {22,33}
print(setB.issuperset(setA))
print(setA.issuperset(setB))
print(setA.issubset(setB))
print(setB.issubset(setA))