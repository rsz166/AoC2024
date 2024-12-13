import re
input = [[[int(x) for x in re.search('.*[\\+=](\\d+),.*[\\+=](\\d+)',c).groups()] for c in l.split('\n')] for l in open('in13.txt').read().strip().split('\n\n')]

def getCost(machine):
    ax = machine[0][0]
    ay = machine[0][1]
    bx = machine[1][0]
    by = machine[1][1]
    x = machine[2][0] + 10000000000000
    y = machine[2][1] + 10000000000000
    
    # a * ax + b * bx == x
    # a * ay + b * by == y
    c = ax / ay
    b = round((x - c * y) / (bx - c * by))
    a = round((x - b * bx) / ax)
    cost = a * 3 + b * 1
    # print(f'{a} {b} {cost}')
    if a * ax + b * bx == x and a * ay + b * by == y:
        return cost
    return 0

total = 0
for machine in input:
    c = getCost(machine)
    print(c)
    total += c
print(f'### {total} ###')