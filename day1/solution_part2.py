import utils

def sum_of_top_3_elf_calories(inventory_list: list[list[int]]) -> int:
    total_calories_per_elf: list[int] = [sum(inventory) for inventory in inventory_list]
    total_calories_per_elf.sort(reverse=True)
    maximum_calories: int = sum(total_calories_per_elf[0:3])
    return maximum_calories

if __name__ == '__main__':
    with open("./input.txt") as f:
        raw_input: str = f.read()
    parsed_input: list[list[int]] = utils.parse_input(raw_input=raw_input)
    answer: int = sum_of_top_3_elf_calories(inventory_list=parsed_input)
    print(f"{answer=}")