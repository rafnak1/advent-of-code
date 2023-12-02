with open('input') as f:
    fish = list(map(int, f.read().split(',')))

n = 80

for c in range(n):
    for i in range(len(fish)):
        fish[i] -= 1
        if fish[i] == -1:
            fish[i] = 6
            fish.append(8)

print(len(fish))
