with open('input') as f:
    data = f.read()

lines = data.splitlines()
dots = [tuple(int(l) for l in line.split(',')) for line in lines[:lines.index('')]]

xfold = 655
dotcount = len(dots)

for dot in dots:
    if dot[0] == xfold:
        dotcount -= 1

for dot in dots:
    if (2*xfold - dot[0], dot[1]) in dots:
        dotcount -= .5

print(int(dotcount))
