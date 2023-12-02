with open('input') as f:
    data = f.read()

lines = data.splitlines()
n, m = len(lines), len(lines[0])

grid = [[0 for i in range(m+2)] for j in range(n+2)] #padding
for j in range(n):
    for i in range(m):
        grid[j+1][i+1] = int(lines[j][i])

stepcount = 0
while not all([all([grid[i+1][j+1] == 0 for j in range(m)]) for i in range(n)]):

    for j in range(n):
        for i in range(m):
            grid[j+1][i+1] += 1

    while any([any([grid[i+1][j+1] > 9 for j in range(m)]) for i in range(n)]):
        for j in range(n):
            for i in range(m):
                if grid[j+1][i+1] > 9:
                    grid[j+1][i+1] = float('-inf')
                    for jj in (j, j+1, j+2):
                        for ii in (i, i+1, i+2):
                            grid[jj][ii] += 1

    for j in range(n):
        for i in range(m):
            if grid[j+1][i+1] == float('-inf'): grid[j+1][i+1] = 0

    stepcount += 1

print(stepcount)
