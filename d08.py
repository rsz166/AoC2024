import math

mapArray = []
markers = []
for i,l in enumerate(open('in08.txt')):
    mapArray.append(list(l.strip()))
    for j,c in enumerate(l.strip()):
        if c != '.':
            markers.append([c,i,j])
height = len(mapArray)
width = len(mapArray[0])
maxSize = max(height, width)
# print(f'{height}x{width}')

def get_harmonics(a,b):
    # part1
    # return [[2 * a[0] - b[0], 2 * a[1] - b[1]]]
    # part2
    step = [a[0]-b[0],a[1]-b[1]]
    div = math.gcd(step[0], step[1])
    step[0] = int(step[0]/div)
    step[1] = int(step[1]/div)
    count = int(maxSize / max(step[0],step[1]))
    return [[a[0]+i*step[0],a[1]+i*step[1]] for i in range(-count,count+1)]

markerDict = {}
for m in markers:
    if not m[0] in markerDict:
        markerDict[m[0]] = [[m[1],m[2]]]
    else:
        markerDict[m[0]].append([m[1],m[2]])

total = 0
validHarmonics = []
for m in markerDict:
    # print(f'{m}: {markerDict[m]}')
    for a in markerDict[m]:
        for b in markerDict[m]:
            if a != b:
                harmonics = get_harmonics(a,b)
                for h in harmonics:
                    if h[0] >= 0 and h[0] < height and h[1] >= 0 and h[1] < width:
                        if not h in validHarmonics:
                            validHarmonics.append(h)
print(len(validHarmonics))
# print(validHarmonics)

# for h in validHarmonics:
#     if mapArray[h[0]][h[1]] == '.':
#         mapArray[h[0]][h[1]] = '#'
#     else:
#         mapArray[h[0]][h[1]] = '@'
# for l in mapArray:
#     print(''.join(l))