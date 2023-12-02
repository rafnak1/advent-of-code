# a(n) is the amount of individuals by day n
# q(n) corresponds to the number of zeroes in day n

n = 256

qmem = [-1 for i in range(n + 10)]

def a(n):
    if n == 0: return 1
    return a(n-1) + q(n-1)

def q(n):
    if n <= 9: return 1 if n == 8 else 0
    if qmem[n] != -1: return qmem[n]
    qmem[n] = q(n-7) + q(n-9)
    return qmem[n]

with open('input') as f:
    initial_fish = list(map(int, f.read().split(',')))

s = 0
for fish in initial_fish:
    s += a(n + 8 - fish)

print(s)
