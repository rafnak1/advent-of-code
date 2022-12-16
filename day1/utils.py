def parse_input(raw_input: str) -> list[list[int]]:    
    pre_parsed_input_1: list[str] = raw_input.strip().split("\n\n")
    pre_parsed_input_2: list[list[str]] = [string_of_integers.split('\n') for string_of_integers in pre_parsed_input_1]
    parsed_input: list[list[int]] = [list(map(int, list_of_strings)) for list_of_strings in pre_parsed_input_2]
    return parsed_input