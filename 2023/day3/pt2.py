import re

def get_part_number_to_the_left(line: str, rightmost_i: int) -> int:
    for i in range(rightmost_i, -1, -1):
        if not line[i].isnumeric():
            i += 1
            break
    return int(line[i: rightmost_i+1])

def get_part_number_to_the_right(line: str, leftmost_i: int) -> int:
    for i in range(leftmost_i, len(line)):
        if not line[i].isnumeric():
            i -= 1
            break
    return int(line[leftmost_i: i+1])

def get_part_numbers_from_section(line: str, start_i: int) -> list[int]:
    section = line[start_i: start_i+3]

    if re.search('[^\d][^\d][^\d]', section):
        return []
    if re.search('[^\d][^\d][\d]', section):
        return [get_part_number_to_the_right(line, start_i+2)]
    if re.search('[^\d][\d][^\d]', section):
        return [int(section[1])]
    if re.search('[^\d][\d][\d]', section):
        return [get_part_number_to_the_right(line, start_i+1)]
    if re.search('[\d][^\d][^\d]', section):
        return [get_part_number_to_the_left(line, start_i)]
    if re.search('[\d][^\d][\d]', section):
        return [get_part_number_to_the_left(line, start_i), get_part_number_to_the_right(line, start_i+2)]
    if re.search('[\d][\d][^\d]', section):
        return [get_part_number_to_the_left(line, start_i+1)]
    # Supposing there are no numbers with four or more digits 
    if re.search('[\d][\d][\d]', section):
        return [int(section)]

# Supposing there are no '*' in map borders
def get_adjacent_parts(engine_map: list[str], i: int, j: int) -> list[int]:
    adjacent_parts = []

    if engine_map[i][j-1].isnumeric():
        adjacent_parts.append(get_part_number_to_the_left(engine_map[i], j-1))
    if engine_map[i][j+1].isnumeric():
        adjacent_parts.append(get_part_number_to_the_right(engine_map[i], j+1))
    
    adjacent_parts.extend(get_part_numbers_from_section(engine_map[i-1], j-1))
    adjacent_parts.extend(get_part_numbers_from_section(engine_map[i+1], j-1))
    
    return adjacent_parts

if __name__ == '__main__':
    with open('input.txt') as f:
        engine_map = f.read().splitlines()

    height = len(engine_map)
    width = len(engine_map[0])

    sum_of_ratios = 0

    for i in range(height):
        for j in range(width):
            if engine_map[i][j] == '*':
                adjacent_parts = get_adjacent_parts(engine_map, i, j)
                if len(adjacent_parts) == 2:
                    sum_of_ratios += adjacent_parts[0] * adjacent_parts[1]

    print(sum_of_ratios)