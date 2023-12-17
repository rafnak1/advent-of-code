def line_to_winning_numbers(line: str) -> list[int]:
    return list(map(int, line.split('|')[0].split(':')[1].split()))

def line_to_obtained_numbers(line: str) -> list[int]:
    return list(map(int, line.split('|')[1].split()))

def compute_points(winning_numbers: list[int], obtained_numbers: list[int]) -> int:
    matches = 0
    for number in obtained_numbers:
        if number in winning_numbers:
            matches += 1
    return 0 if matches == 0 else 2**(matches - 1)