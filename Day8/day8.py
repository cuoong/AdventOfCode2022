import sys

file = sys.argv[1] if len(sys.argv) > 1 else '8.in'
data = open(file).readlines()

line = [x.strip() for x in data]

numberOfRows = len(line)
numberOfColumns = len(line[0])

# *****
# *   *
# *   *
# *   *
# *****

edges = (numberOfRows * 2) + ((numberOfColumns - 2) * 2)
result = 0
scores = []

for row in range(1, numberOfRows - 1):
    for column in range(1, numberOfColumns - 1):
        position = line[row][column]

        left = [line[row][column-i] for i in range(1, column+1)]
        right = [line[row][column+i]
                 for i in range(1, numberOfColumns - column)]
        top = [line[row-i][column] for i in range(1, row+1)]
        down = [line[row+i][column] for i in range(1, numberOfRows - row)]

        # print(position)
        # print(right)
        # print(left)
        # print(top)
        # print(down)
        if max(left) < position or max(right) < position or max(top) < position or max(down) < position:
            result += 1

        score = 1
        for list in (left, right, top, down):
            maker = 0
            for i in range(len(list)):

                if list[i] < position:
                    maker += 1
                elif list[i] >= position:
                    maker += 1
                    break
            score *= maker
        scores.append(score)

print(max(scores))
print(result + edges)
