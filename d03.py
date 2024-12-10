import re

with open('in03.txt') as f:
    text = f.read().strip()

sum = 0
enabled = True

# for match in re.findall('[mul\(([0-9]+),([0-9]+)\),]', text):
#     sum += int(match[0]) * int(match[1])

for match in re.findall('mul\\(([0-9]+),([0-9]+)\\)|(do(n\'t)?\\(\\))', text):
    if match[2] == 'don\'t()':
        enabled = False
    elif match[2] == 'do()':
        enabled = True
    elif enabled:
        sum += int(match[0]) * int(match[1])

print(sum)