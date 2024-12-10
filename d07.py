lines = [[int(x.strip(' :\n')) for x in l.strip().split(' ')] for l in open('in07.txt')]


def check_equ_rec(equ, prevSum, result):
    if len(equ) == 0:
        return prevSum == result
    if check_equ_rec(equ[1:], prevSum+equ[0], result):
        return True
    if check_equ_rec(equ[1:], prevSum*equ[0], result):
        return True
    if check_equ_rec(equ[1:], int(str(prevSum) + str(equ[0])), result):
        return True
    return False

total = 0
for l in lines:
    if check_equ_rec(l[2:],l[1],l[0]):
        total += l[0]
print(total)
