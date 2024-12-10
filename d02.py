
def count_nok(levels):
    diff = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
    cnt = 0
    if diff[0] < 0:
        # decreasing
        for x in diff:
            if x>=0 or x<-3:
                cnt += 1
    else:
        # increasing
        for x in diff:
            if x<=0 or x>3:
                cnt += 1
    return cnt


safe = 0

for line in open('in02.txt'):
    levels = [int(x) for x in line.strip().split(' ')]
    nok = count_nok(levels)
    if nok == 0:
        safe += 1
    else:
        can_be_safe = False
        for i in range(len(levels)):
            modified = [x for j,x in enumerate(levels) if j!=i]
            if count_nok(modified) == 0:
                can_be_safe = True
        if can_be_safe:
            safe += 1

print(safe)
