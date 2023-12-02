with open('input.txt') as f:
    lines = f.read().splitlines()

proposed_amounts = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

# sample_string: ' 1 blue, 2 green'
def sample_is_possible(sample_string: str) -> bool:
    splitted_sample = sample_string.split(',')
    for color_amount_data in splitted_sample:
        [color_amount, color_name] = color_amount_data.strip().split()
        if not int(color_amount) <= proposed_amounts[color_name]:
            return False
    return True

def game_is_possible(line):
    return all(map(sample_is_possible, line.split(':')[1].split(';')))

id_sum = 0
for i, line in enumerate(lines):
    if game_is_possible(line):
        id_sum += i + 1  # because index i is actually game i+1

print(id_sum)