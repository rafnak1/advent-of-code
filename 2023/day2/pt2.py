with open('input.txt') as f:
    lines = f.read().splitlines()

# sample_string: ' 1 blue, 2 green'
def process_sample(sample_string: str) -> dict:
    processed_sample = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    splitted_sample = sample_string.split(',')
    for color_amount_data in splitted_sample:
        [color_amount, color_name] = color_amount_data.strip().split()
        processed_sample[color_name] = int(color_amount)
    return processed_sample

def minimum_set_power(line):
    minimum_set = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    for sample in map(process_sample, line.split(':')[1].split(';')):
        for color in minimum_set:
            if minimum_set[color] < sample[color]:
                minimum_set[color] = sample[color]
    return minimum_set['red'] * minimum_set['green'] * minimum_set['blue']

power_sum = 0
for line in lines:
    power_sum += minimum_set_power(line) 

print(power_sum)