with open('in09.txt') as f:
    disk = [int(x) for x in f.read().strip()]

# checksum = 0
# sectorIndex = 0
# diskIndex = 0
# diskEndIndex = (len(disk) & ~1) + 2 # only even indexes contains file, initialize after last file
# diskEndSectorRemaining = 0

# def get_cs(dataIdx):
#     global sectorIndex
#     cs = dataIdx * sectorIndex
#     sectorIndex += 1
#     # print(dataIdx, end='')
#     return cs

# def get_data_cs():
#     global diskIndex
#     data_cs = 0
#     dataIdx = int(diskIndex/2)
#     for _ in range(disk[diskIndex]):
#         data_cs += get_cs(dataIdx)
#     diskIndex += 1
#     return data_cs

# def get_space_cs():
#     global diskIndex,diskEndIndex,diskEndSectorRemaining
#     space_cs = 0
#     for _ in range(disk[diskIndex]):
#         while diskEndSectorRemaining == 0 and diskIndex < diskEndIndex:
#             diskEndIndex -= 2
#             diskEndSectorRemaining = disk[diskEndIndex]
#         if diskEndIndex < diskIndex:
#             break
#         space_cs += get_cs(int(diskEndIndex/2))
#         diskEndSectorRemaining -= 1
#     diskIndex += 1
#     return space_cs

# def get_remaining_cs():
#     global diskEndIndex,diskEndSectorRemaining
#     rem_cs = 0
#     while diskEndSectorRemaining > 0:
#         rem_cs += get_cs(int(diskEndIndex/2))
#         diskEndSectorRemaining -= 1
#     return rem_cs

# while diskIndex < diskEndIndex:
#     if diskIndex % 2 == 0:
#         checksum += get_data_cs()
#     else:
#         checksum += get_space_cs()
# checksum += get_remaining_cs()

# print()
# print(checksum) # part1

# part2
diskBlocks = [[x,int(i/2) if i%2==0 else -1] for i,x in enumerate(disk)]
# for x in diskBlocks:
#     print(x[0] * ('.' if x[1] == -1 else str(x[1])),end='')
# print()

fileId = [x[1] for x in diskBlocks if x[1] >= 0][-1] # find last file ID
while fileId >= 0:
    fileIdx,file = [(i,x) for i,x in enumerate(diskBlocks) if x[1] == fileId][0]
    spaces = [i for i,x in enumerate(diskBlocks) if x[1] == -1 and x[0] >= file[0]]
    if spaces:
        targetIdx = spaces[0]
        if targetIdx < fileIdx:
            if file[0] == diskBlocks[targetIdx][0]:
                diskBlocks[targetIdx][1] = file[1]
            else:
                diskBlocks[targetIdx][0] -= file[0]
                diskBlocks.insert(targetIdx,[file[0],file[1]])
            file[1] = -1
    fileId -= 1

# for x in diskBlocks:
#     print(x[0] * ('.' if x[1] == -1 else str(x[1])),end='')
# print()
checksum = 0
sectorIdx = 0
for block in diskBlocks:
    if block[1] > 0:
        checksum += sum(range(sectorIdx,sectorIdx+block[0])) * block[1]
    sectorIdx += block[0]
print(checksum)