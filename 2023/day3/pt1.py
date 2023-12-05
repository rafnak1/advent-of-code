def get_new_index_and_number_value(line: str, initial_j: int):
    final_j = initial_j
    while final_j < len(line) and line[final_j].isnumeric():
        final_j += 1
    return final_j, int(line[initial_j: final_j])

def get_new_index_and_amount_to_add(engine_map, initial_i: int, initial_j: int):
    height = len(engine_map)
    width = len(engine_map[0])
    final_j, number_value = get_new_index_and_number_value(engine_map[initial_i], initial_j)
    
    lower_limit = 0 if initial_i == 0 else initial_i-1
    upper_limit = initial_i+1 if initial_i+1 == height else initial_i+2
    leftmost_limit = 0 if initial_j == 0 else initial_j-1
    rightmost_limit = final_j if final_j == width else final_j+1

    for i in range(lower_limit, upper_limit):
        for j in range(leftmost_limit, rightmost_limit):
            if engine_map[i][j] not in '0123456789.':
                return final_j, number_value
    
    return final_j, 0

if __name__ == '__main__':
    with open('input.txt') as f:
        engine_map = f.read().splitlines()

    height = len(engine_map)
    width = len(engine_map[0])

    sum_of_parts = 0

    for i in range(height):
        j = 0
        while j < width:
            if engine_map[i][j].isnumeric():
                j, amount_to_add = get_new_index_and_amount_to_add(engine_map, i, j)
                sum_of_parts += amount_to_add
                if j == width: # iteration wrapped
                    break
            j += 1
    
    print(sum_of_parts)