import utils

def maximum_amount_of_calories_in_one_inventory(inventory_list: list[list[int]]) -> int:
    total_calories_per_elf = [sum(inventory) for inventory in inventory_list]
    maximum_calories = max(total_calories_per_elf)
    return maximum_calories

if __name__ == '__main__':
    with open("./input.txt") as f:
        raw_input: str = f.read()
    parsed_input: list[list[int]] = utils.parse_input(raw_input=raw_input)
    answer: int = maximum_amount_of_calories_in_one_inventory(inventory_list=parsed_input)
    print(f"{answer=}")