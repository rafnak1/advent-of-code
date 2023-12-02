def array_not(arr):
    r = []
    for item in arr:
        if item == 0:
            r.append(1)
        else:
            r.append(0)
    return r

def bin2int(arr):
    r = 0
    for i in range(len(arr)):
        if arr[len(arr) - 1 - i] == 1:
            r += 2**i
    return r

with open('input.txt') as f:
    a = f.read()

a = a.split('\n')
a.pop()

gamma_bin = [0 for i in range(12)]

for i in range(12):

    ones, zeroes = 0, 0
    for word in a:
        if word[i] == '1':
            ones += 1
        else:
            zeroes += 1

    if ones == zeroes:
        print("well that's bad")
    elif ones > zeroes:
        gamma_bin[i] = 1
    else:
        gamma_bin[i] = 0

gamma = bin2int(gamma_bin)
epsilon_bin = array_not(gamma_bin)
epsilon = bin2int(epsilon_bin)

print(gamma * epsilon)
