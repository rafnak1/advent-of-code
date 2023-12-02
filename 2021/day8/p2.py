def digit_resolve(line):
    tendigits = list(map(set, line[:line.index('|')].split()))
    D = [None for i in range(10)]

    for d in tendigits:
        if len(d) == 2: D[1] = d
        if len(d) == 4: D[4] = d
        if len(d) == 3: D[7] = d
        if len(d) == 7: D[8] = d

    for d in tendigits:
        if len(d) == 6:
            if len(d.intersection(D[8]).intersection(D[1])) == 1: D[6] = d
            if d.issuperset(D[4]): D[9] = d

    for d in tendigits:
        if len(d) == 6 and d != D[6] and d != D[9]: D[0] = d

    for d in tendigits:
        if len(d) == 5 and len(d.intersection(D[1])) == 2: D[3] = d

    for d in tendigits:
        if len(d) == 5 and d != D[3]:
            if len(d.intersection(D[4])) == 2: D[2] = d
            if len(d.intersection(D[4])) == 3: D[5] = d

    if None in D: print('Whoops. There is None in D')

    return D

def number(line, digit_map):
    scrambled_number = list(map(set, line[line.index('|')+1:].split()))
    digit2str = list(map(str, [i for i in range(10)]))
    r = ''
    for d in scrambled_number:
        r += digit2str[digit_map.index(d)]
    return int(r)

with open('input') as f:
    data = f.read()

lines = data.splitlines()

count = sum(number(line, digit_resolve(line)) for line in lines)

print(count)
