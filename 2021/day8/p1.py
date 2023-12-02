with open('input') as f:
    data = f.read()

lines = data.splitlines()

count = 0
for line in lines:
    output = line[line.index('|'):].split()
    for digit in output:
        if len(digit) in {2,4,3,7}:
            count += 1

print(count)
