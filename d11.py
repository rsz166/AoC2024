input = [int(x) for x in open('in11.txt').read().strip().split(' ') if x]

# def evolve(x,blinks):
#     while blinks > 0:
#         blinks -= 1
#         if x == 0:
#             x = 1
#         else:
#             s = str(x)
#             l = len(s)
#             if l % 2 == 0:
#                 l1 = int(l/2)
#                 x1 = int(s[:l1])
#                 x2 = int(s[l1:])
#                 return evolve(x1,blinks)+evolve(x2,blinks)
#             else:
#                 x *= 2024
#     # print(f'{x} ',end='')
#     return 1

# total = 0
# for x in input:
#     total += evolve(x,75)
# # print()
# print(total)


# solution 2

def add(d, key, count):
    if key in d:
        d[key] += count
    else:
        d[key] = count

def evolve2(d, x, count):
    if x == 0:
        add(d,1,count)
    else:
        s = str(x)
        l = len(s)
        if l % 2 == 0:
            l1 = int(l/2)
            x1 = int(s[:l1])
            x2 = int(s[l1:])
            add(d,x1,count)
            add(d,x2,count)
        else:
            add(d,x*2024,count)

last = {}
for x in input:
    if x in last:
        last[x] += 1
    else:
        last[x] = 1
blinks = 75
while blinks > 0:
    blinks -= 1
    current = {}
    for x in last:
        evolve2(current,x,last[x])
    last = current
print(sum([last[x] for x in last]))
