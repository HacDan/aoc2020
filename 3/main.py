
f = open("input.txt")
mapSegment = []
lineNum = -1
for l in f:
    lineMapSegment = []
    l = l.strip()
    for c in l:
        colNum = 0
        lineMapSegment.append(c.strip())
    mapSegment.append(lineMapSegment)
tree = "#"
blank = "."
treeCount = 0

x = 3
y = 1
while x <= 31:
    x += 3
    y += 1
    print(x)
    print(y)
    if mapSegment[y][x] == tree:
        treeCount += 1
        print("Found a tree at: ", x, y)

print(treeCount)