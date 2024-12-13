import re
input = [[[int(x) for x in re.search('.*[\\+=](\\d+),.*[\\+=](\\d+)',c).groups()] for c in l.split('\n')] for l in open('in13.txt').read().strip().split('\n\n')]

def getCost(machine):
    ax = machine[0][0]
    ay = machine[0][1]
    bx = machine[1][0]
    by = machine[1][1]
    x = machine[2][0]
    y = machine[2][1]
    a = min(x // ax, 100)
    b = min((x - a * ax) // bx, 100)
    minCost = 1000 # 400 = 100 * (3 + 1) is the max number of button presses * token costs
    while a >= 0:
        if a * ax + b * bx == x and a * ay + b * by == y:
            cost = a * 3 + b * 1
            if cost < minCost:
                minCost = cost
        a -= 1
        b = min((x - a * ax) // bx, 100)
    return 0 if minCost == 1000 else minCost

total = 0
for machine in input:
    c = getCost(machine)
    print(c)
    total += c
print(f'### {total} ###')