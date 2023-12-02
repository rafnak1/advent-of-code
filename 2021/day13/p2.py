def fold(dots, instruction):
    r = set()
    for dot in dots:
        if instruction[0] == 'x':
            if dot[0] != instruction[1]:
                r.add((instruction[1] - abs(instruction[1] - dot[0]), dot[1]))
        if instruction[0] == 'y':
            if dot[1] != instruction[1]:
                r.add((dot[0], instruction[1] - abs(instruction[1] - dot[1])))
    return r

def print_dots(dots):
    xmax, ymax = max(dot[0] for dot in dots), max(dot[1] for dot in dots)
    for j in range(ymax + 1):
        for i in range(xmax + 1):
            if (i, j) in dots: print('#', end='')
            else: print('.', end='')
        print()

with open('input') as f:
    data = f.read()

lines = data.splitlines()
dots = set(tuple(int(l) for l in line.split(',')) for line in lines[:lines.index('')])
instructions = [(line.split()[2].split('=')[0], int(line.split()[2].split('=')[1])) for line in lines[lines.index('')+1:]]

for instruction in instructions:
    dots = fold(dots, instruction)

print_dots(dots)
