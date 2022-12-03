def parse_input(raw_input: str) -> list[list[int]]:    
    pre_parsed_input_1: list[str] = raw_input.strip().split("\n\n")
    pre_parsed_input_2: list[list[str]] = [string_of_integers.split('\n') for string_of_integers in pre_parsed_input_1]
    parsed_input: list[list[int]] = [list(map(int, list_of_strings)) for list_of_strings in pre_parsed_input_2]
    return parsed_input

def maximum_amount_of_calories_in_one_inventory(inventory_list: list[list[int]]) -> int:
    total_calories_per_elf = [sum(inventory) for inventory in inventory_list]
    maximum_calories = max(total_calories_per_elf)
    return maximum_calories

if __name__ == '__main__':
    with open("./input.txt") as f:
        raw_input = f.read()
    parsed_input = parse_input(raw_input=raw_input)
    answer = maximum_amount_of_calories_in_one_inventory(inventory_list=parsed_input)
    print(f"{answer=}")