from utils import *

#lines are represented by a tuple of two tuples
L = 1000
FILENAME = "input.txt"

seafloor = [[0 for i in range(L)] for i in range(L)]

lines = fetch_lines(FILENAME)

for line in lines:
    mark_map(seafloor, line)

count = 0
for j in range(L):
    for i in range(L):
        if seafloor[j][i] > 1:
            count += 1

print(count)
