mapArray = [[int(c) for c in l] for l in open('in10.txt').read().split('\n') if l]
lines = len(mapArray)
cols = len(mapArray[0])

def findPaths(lineIdx,colIdx,value=0):
    if lineIdx < 0 or lineIdx >= lines or colIdx < 0 or colIdx >= cols:
        return []
    if value != mapArray[lineIdx][colIdx]:
        return []
    if value == 9:
        return [[lineIdx,colIdx]]
    ret = []
    ret.extend(findPaths(lineIdx-1,colIdx,value+1))
    ret.extend(findPaths(lineIdx+1,colIdx,value+1))
    ret.extend(findPaths(lineIdx,colIdx-1,value+1))
    ret.extend(findPaths(lineIdx,colIdx+1,value+1))
    return ret

total = 0
total2 = 0
for i,l in enumerate(mapArray):
    for j,c in enumerate(l):
        if c == 0:
            reachable = findPaths(i,j)
            unique = []
            for x in reachable:
                if not x in unique:
                    unique.append(x)
            total += len(unique)
            total2 += len(reachable)
print(total2)