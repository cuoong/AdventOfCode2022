file = open("/Users/cuong/Documents/AdventOfCode2022/Day6/input.txt")
line = file.read()
i = 0
while True:
    str = line[i:i+14]
    if len(set(list(str))) == 14:
        print(i+14)
        break
    i += 1
