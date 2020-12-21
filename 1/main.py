from itertools import combinations

f = open("input.txt", "r")
nums = []
for l in f:
    nums.append(int(l))
for comb in combinations(nums, 2):
    if sum(list(comb)) == 2020:
        print(list(comb)[0] * list(comb)[1])

nums = []
for l in f:
    nums.append(int(l))
for comb in combinations(nums, 3):
    if sum(list(comb)) == 2020:
        print(list(comb)[0] * list(comb)[1] * list(comb)[2])