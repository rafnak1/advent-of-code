from functions import line_to_winning_numbers, line_to_obtained_numbers, compute_points

with open('input.txt') as f:
    scratchpads = f.read().splitlines()

winning_numbers = list(map(line_to_winning_numbers, scratchpads))
obtained_numbers = list(map(line_to_obtained_numbers, scratchpads))

total_points = 0
for i in range(len(scratchpads)):
    total_points += compute_points(winning_numbers[i], obtained_numbers[i])

print(total_points)