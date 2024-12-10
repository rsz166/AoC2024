values1 = []
values2 = []
for line in open('in01.txt'):
    x1,x2 = line.split('   ')
    values1.append(int(x1))
    values2.append(int(x2))

# total = 0
# while values1:
#     x1 = min(values1)
#     x2 = min(values2)
#     total += abs(x1-x2)
#     values1.remove(x1)
#     values2.remove(x2)

# print(total)

### part2

total = 0
for x1 in values1:
    total += x1 * sum([1 for x2 in values2 if x2==x1])

print(total)
