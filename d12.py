input = [[c for c in l] for l in open('in12.txt').read().split('\n') if l]
lines = len(input)
cols = len(input[0])

zones = [[0 for _ in range(cols)] for _ in range(lines)]

def markAndSpread(line,col,id,plant):
    if line < 0 or line >= lines or col < 0 or col >= cols:
        return
    if input[line][col] != plant:
        return
    if zones[line][col] != 0:
        return
    zones[line][col] = id
    markAndSpread(line-1,col,id,plant)
    markAndSpread(line+1,col,id,plant)
    markAndSpread(line,col-1,id,plant)
    markAndSpread(line,col+1,id,plant)

zoneCount = 0
def createZone(line,col):
    global zoneCount
    zoneCount += 1
    # plant = input[line][col]
    markAndSpread(line,col,zoneCount,input[line][col])

for i,l in enumerate(zones):
    for j,c in enumerate(l):
        if c == 0:
            createZone(i,j)

# calculate size and perimeter

def getZonePoints(zone):
    ret = []
    for i,l in enumerate(zones):
        for j,c in enumerate(l):
            if c == zone:
                ret.append([i,j])
    return ret

def getPerimeter(points):
    missingPairs = 0
    for p in points:
        for n in [
            [p[0]-1,p[1]],
            [p[0]+1,p[1]],
            [p[0],p[1]-1],
            [p[0],p[1]+1]
        ]:
            if not n in points:
                missingPairs += 1
    return missingPairs

# part 1
# cost = 0
# for zone in range(1,zoneCount+1):
#     points = getZonePoints(zone)
#     size = len(points)
#     perimeter = getPerimeter(points)
#     cost += size * perimeter
#     # print(f'zone {zone} size {size} perim {perimeter}')
# print(cost)

def getSides(points):
    edgesH = []
    edgesV = []
    for p in points:
        for n in [
            [p[0]-1,p[1]],
            [p[0]+1,p[1]]
        ]:
            if not n in points:
                edgesH.append([min(p[0],n[0]),p[1]])
        for n in [
            [p[0],p[1]-1],
            [p[0],p[1]+1]
        ]:
            if not n in points:
                edgesV.append([min(p[1],n[1]),p[0]]) # invert lines and cols for easier calculation
    # check each line, find if continuous
    ret = 0
    for idx in set([x[0] for x in edgesH]):
        # edges in this line
        e = sorted([x[1] for x in edgesH if x[0] == idx])
        ret += 1
        for i in range(len(e)-1):
            if e[i+1]-e[i] != 1:
                ret += 1
            elif [e[i],idx] in edgesV and [e[i],idx+1] in edgesV:
                ret += 1
            else:
                pass
    for idx in set([x[0] for x in edgesV]):
        # edges in this line
        e = sorted([x[1] for x in edgesV if x[0] == idx])
        ret += 1
        for i in range(len(e)-1):
            if e[i+1]-e[i] != 1 or ([e[i],idx] in edgesH or [e[i],idx+1] in edgesH):
                ret += 1
    return ret

# part2
zoneDetails = []
cost = 0
for zone in range(1,zoneCount+1):
    points = getZonePoints(zone)
    size = len(points)
    sides = getSides(points)
    cost += size * sides
    zoneDetails.append([[input[points[0][0]][points[0][1]]],size,sides,points])
    # print(f'zone {zone} plant {input[points[0][0]][points[0][1]]} size {size} sides {sides}')
print(cost)

# debug code
def printZone(points):
    minLine = min([x[0] for x in points])
    minCol = min([x[1] for x in points])
    maxLine = max([x[0] for x in points])
    maxCol = max([x[1] for x in points])
    for l in range(minLine, maxLine+1):
        for c in range(minCol, maxCol+1):
            if [l,c] in points:
                print('x',end='')
            else:
                print(' ',end='')
        print()
    print() # empty line

# sidesList = sorted(list(set([x[2] for x in zoneDetails])))
# print(sidesList)
# for s in sidesList:
#     print(f'################# edge {s} #################')
#     similarZones = [x[3] for x in zoneDetails if x[2] == s]
#     for z in similarZones:
#         printZone(z)

# for l in input:
#     print(''.join(l))

# for l in zones:
#     print(''.join([str(x%10) for x in l]))

