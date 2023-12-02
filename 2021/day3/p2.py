def filter_measurements_oxygen(measurements, i):
    if len(measurements) == 1:
        return measurements

    ones, zeroes = 0, 0
    for m in measurements:
        if m[i] == '1':
            ones += 1
        else:
            zeroes += 1
    if ones >= zeroes:
        for m in measurements.copy():
            if m[i] == '0':
                measurements.remove(m)
    else:
        for m in measurements.copy():
            if m[i] == '1':
                measurements.remove(m)
    return measurements

def filter_measurements_carbon(measurements, i):
    if len(measurements) == 1:
        return measurements

    ones, zeroes = 0, 0
    for m in measurements:
        if m[i] == '1':
            ones += 1
        else:
            zeroes += 1
    if zeroes <= ones:
        for m in measurements.copy():
            if m[i] == '1':
                measurements.remove(m)
        print(measurements)
    else:
        for m in measurements.copy():
            if m[i] == '0':
                measurements.remove(m)
        print(measurements)
    return measurements

with open('input.txt') as f:
    a = f.read()

a = a.split('\n')
a.pop()

length = len(a)
width = len(a[0])

temp = a.copy()
for i in range(width):
    temp = filter_measurements_oxygen(temp, i)
oxygen_rating = int(temp[0], 2)

temp = a.copy()
for i in range(width):
    temp = filter_measurements_carbon(temp, i)
carbon_rating = int(temp[0], 2)

print(oxygen_rating)
print(carbon_rating)
print(oxygen_rating * carbon_rating)
