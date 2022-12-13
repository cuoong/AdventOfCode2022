import sys
from collections import defaultdict

file = sys.argv[1] if len(sys.argv) > 1 else '7.in'
data = open(file).read()
lines = [x for x in data.split('\n')]

path = []
dict = defaultdict(int)

for line in lines:
    words = line.strip().split()
    if words[1] == 'cd':
        if words[2] == '..':
            # back to previous
            path.pop()
        else:
            path.append(words[2])
    elif words[1] == 'ls':
        continue
    elif words[0] == 'dir':
        continue
    else:
        file_size = int(words[0])
        for i in range(1, len(path) + 1):
            directory = ''.join(path[:i])
            dict[directory] += file_size

print(dict.items())
result = 0
for key, value in dict.items():
    if value <= 100000:
        result += value

print(result)
