def basin_area(x, y):
    global cavemap
    scanned = set([(x,y)])
    li, lf = 1, 0
    while li != lf:
        li = len(scanned)
        for coord in scanned:
            i, j = coord[0], coord[1]
            a,b,c,d = (i+1, j),(i, j-1),(i-1, j),(i, j+1)
            t = [e if e[0] in range(m) and e[1] in range(n) else (i,j) for e in (a,b,c,d)]
            scanned = scanned.union(set(e if cavemap[e[1]][e[0]] != 9 else (i,j) for e in t))
        lf = len(scanned)
    return lf

with open('input') as f:
    data = f.read()

cavemap = [[int(height) for height in line] for line in data.splitlines()]
n, m = len(cavemap), len(cavemap[0])

basin_areas = []
for j in range(n):
    for i in range(m):
        a,b,c,d = (i+1, j),(i, j-1),(i-1, j),(i, j+1)
        ha, hb, hc, hd = tuple(cavemap[e[1]][e[0]] if e[0] in range(m) and e[1] in range(n) else float('inf') for e in (a,b,c,d))
        if all(tuple(cavemap[j][i] < he for he in (ha,hb,hc,hd))):
            basin_areas.append(basin_area(i, j))

ordered = sorted(basin_areas)
print(ordered[-1] * ordered[-2] * ordered[-3])
