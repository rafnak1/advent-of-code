with open('input.txt') as f:
    lines = f.readlines()

def get_number(line):
    for c in line:
        if c.isdigit():
            first_digit = c
            break
    for c in line[::-1]:
        if c.isdigit():
            second_digit = c
            break
    return int(first_digit + second_digit)

total = sum(list(map(get_number, lines)))
print(total)