lines = [x.strip() for x in open('in04.txt')]
iMax = len(lines)-1
jMax = len(lines[0])-1
xmas = 'XMAS'
xmasLen = len(xmas)
directions = [
    [0,1],[0,-1],
    [1,0],[-1,0],
    [1,1],[1,-1],
    [-1,1],[-1,-1]
]

def getc(i,j):
    if i<0 or i>iMax or j<0 or j>jMax: return ' '
    return lines[i][j]

def find_str(i,j):
    x = 0
    for d in directions:
        s = ''.join([getc(i + d[0]*dx,j + d[1] * dx) for dx in range(xmasLen)])
        if s == xmas:
            x += 1
    return x

total = 0
for i,l in enumerate(lines):
    for j,c in enumerate(l):
        if c == 'X':
            total += find_str(i,j)
# print(total)

xmasMatrixes = [
    ['M.S',
     '.A.',
     'M.S'],
    ['M.M',
     '.A.',
     'S.S'],
    ['S.S',
     '.A.',
     'M.M'],
    ['S.M',
     '.A.',
     'S.M']
]
xmasMatSize = 3

def checkMatrix(i,j,mat):
    for di in range(xmasMatSize):
        for dj in range(xmasMatSize):
            if mat[di][dj] != '.':
                if lines[i+di][j+dj] != mat[di][dj]:
                    return False
    return True

def checkMatrixes(i,j):
    for mat in xmasMatrixes:
        if checkMatrix(i,j,mat):
            return True
    return False

total = 0
for i in range(iMax-xmasMatSize+2):
    for j in range(jMax-xmasMatSize+2):
        if checkMatrixes(i,j):
            total += 1
            # print(i,j)
print(total)
