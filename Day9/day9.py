import sys
import numpy as np

file = sys.argv[1] if len(sys.argv) > 1 else '9.in'
data = open(file).readlines()
head = (0, 0)
tail = (0, 0)
visited = set()
visited.add(tail)

for ele in data:
    dir, steps = ele.split()
    for _ in range(int(steps)):
        match dir:
            case 'U':
                head = (head[0], head[1] + 1)
            case 'D':
                head = (head[0], head[1] - 1)
            case 'L':
                head = (head[0] - 1, head[1])
            case 'R':
                head = (head[0] + 1, head[1])
        diff_x = head[0] - tail[0]
        diff_y = head[1] - tail[1]
        if abs(diff_x) > 1 or abs(diff_y) > 1:
            tail = (tail[0] + np.sign(diff_x), tail[1] + np.sign(diff_y))
            visited.add(tail)
print(len(visited))
