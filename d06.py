mapArray = [list(l.strip()) for l in open('in06.txt')]

# for l in mapArray:
#     print(l)

C_POS = '^'
C_WALL = '#'
C_EMPTY = '.'
C_USED = 'X'

direction = 0 # up: 0, right: 1, ..
running = True
startPosition = [[i,x.index(C_POS)] for i,x in enumerate(mapArray) if C_POS in x][0]
position = startPosition
# print(position)

def get_next(position, direction):
    if direction == 0: # up
        return [position[0]-1,position[1]]
    if direction == 1: # right
        return [position[0],position[1]+1]
    if direction == 2: # down
        return [position[0]+1,position[1]]
    if direction == 3: # left
        return [position[0],position[1]-1]
    raise Exception()

def check_next(nextPos):
    if nextPos[0] < 0 or nextPos[0] >= len(mapArray):
        return 2
    if nextPos[1] < 0 or nextPos[1] >= len(mapArray[0]):
        return 2
    c = mapArray[nextPos[0]][nextPos[1]]
    if c == C_WALL:
        return 0
    return 1

while running:
    mapArray[position[0]][position[1]] = C_USED
    nextPos = get_next(position, direction)
    check = check_next(nextPos)
    if check == 0:
        direction = (direction + 1) % 4
    elif check == 1:
        position = nextPos
    else:
        running = False
total = sum([sum([1 for c in x if c==C_USED]) for x in mapArray])
# print(total)

# for l in mapArray:
#     print(l)

## part 2

def check_infinite(mapArray, position):
    turnPoints = []
    direction = 0
    while True:
        nextPos = get_next(position, direction)
        check = check_next(nextPos)
        if check == 0: # turn
            # check for infinite
            turn = [position[0],position[1],direction]
            if turn in turnPoints:
                return True # infinite
            turnPoints.append(turn)
            # turn
            direction = (direction + 1) % 4
        elif check == 1: # go
            position = nextPos
        else: # end
            return False # not infinite

total = 0
for i in range(len(mapArray)):
    for j in range(len(mapArray[0])):
        if mapArray[i][j] == C_USED:
            # try to place wall and check if infinite
            mapArray[i][j] = C_WALL
            if check_infinite(mapArray, startPosition):
                total += 1
            mapArray[i][j] = C_USED
print(total)