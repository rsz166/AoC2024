rules = []
updates = []
with open('in05.txt') as f:
    text = f.read().strip().split('\n\n')
    for l in text[0].strip().split('\n'):
        parts = [int(x) for x in l.strip().split('|')]
        rules.append(parts)
    for l in text[1].strip().split('\n'):
        parts = [int(x) for x in l.strip().split(',')]
        updates.append(parts)

def check_update(update):
    for r in rules:
        if r[0] in update and r[1] in update:
            if update.index(r[0]) > update.index(r[1]):
                return False
    return True

def fix_update(update):
    relevant_rules = [r for r in rules if r[0] in update and r[1] in update]
    working = True
    while working:
        working = False
        for r in relevant_rules:
            i0 = update.index(r[0])
            i1 = update.index(r[1])
            if i0 > i1:
                x = update[i0]
                update[i0] = update[i1]
                update[i1] = x
                working = True
    return update

total = 0
total2 = 0
for update in updates:
    if check_update(update):
        total += update[int(len(update)/2)]
    else:
        fixed = fix_update(update)
        total2 += fixed[int(len(update)/2)]
# print(total)
print(total2)