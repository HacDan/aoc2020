
f = open("input.txt")
mapSegment = []
lineNum = -1
for l in f:
    lineMapSegment = []
    l = l.strip()
    l = l * 250
    for c in l:
        lineMapSegment.append(c.strip())
    mapSegment.append(lineMapSegment)
tree = "#"
blank = "."
treeCount = 0
x = 0
y = 0
while y <= 323:
    x += 3
    y += 1
    print(x, y)
    if mapSegment[y][x] == tree:
        treeCount += 1
        print(treeCount)
