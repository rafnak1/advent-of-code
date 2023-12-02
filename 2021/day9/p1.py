with open('input') as f:
    data = f.read()

cavemap = [[int(height) for height in line] for line in data.splitlines()]
n, m = len(cavemap), len(cavemap[0])

s = 0
for j in range(n):
    for i in range(m):
        a,b,c,d = (i+1, j),(i, j-1),(i-1, j),(i, j+1)
        ha, hb, hc, hd = tuple(cavemap[e[1]][e[0]] if e[0] in range(m) and e[1] in range(n) else float('inf') for e in (a,b,c,d))
        if all(tuple(cavemap[j][i] < he for he in (ha,hb,hc,hd))):
            s += 1 + cavemap[j][i]

print(s)
