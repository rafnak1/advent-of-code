with open('input.txt') as f:
    lines = f.read().splitlines()

spelled_numbers_normal = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

spelled_numbers_reversed = {}
for spelled_number, number in spelled_numbers_normal.items():
    spelled_numbers_reversed[spelled_number[::-1]] = number

def get_first_number_match(line, spelled_numbers):
    for i in range(len(line)):
        if line[i].isdigit():
            return int(line[i])
        for spelled_number, number in spelled_numbers.items():
            if len(spelled_number) <= len(line) - i:
                if line[i : i + len(spelled_number)] == spelled_number:
                    return number
    return 0

def get_first_digit(line):
    return get_first_number_match(line, spelled_numbers_normal)

def get_second_digit(line):
    return get_first_number_match(line[::-1], spelled_numbers_reversed)

def get_number(line):
    first_digit = get_first_digit(line)
    second_digit = get_second_digit(line)
    return first_digit * 10 + second_digit

if __name__ == '__main__':
    total = sum(map(get_number, lines))
    print(total)