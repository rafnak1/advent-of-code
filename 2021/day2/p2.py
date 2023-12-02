with open('input') as f:
    a = f.read()

b = a.split('\n')
b.pop()

x, depth, aim = 0, 0, 0

for line in b:
    c = line.split()
    command = c[0]
    delta = int(c[1])
    if command == 'forward':
        x += delta
        depth += aim * delta
    elif command == 'down':
        aim += delta
    elif command == 'up':
        aim -= delta

print(x * depth)
