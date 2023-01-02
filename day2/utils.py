def parse_input(raw_input: str) -> list[tuple[str, str]]:
    stripped_input: str = raw_input.strip()
    newline_split_input: list[str] = stripped_input.splitlines()
    parsed_input: list[tuple[str, str]] = [(line[0], line[2]) for line in newline_split_input]
    return parsed_input

def outcome_of_round(round_data: tuple[str, str]) -> str:
    outcome_dictionary = {
        ('A', 'X'): 'draw',
        ('A', 'Y'): 'win' ,
        ('A', 'Z'): 'loss',
        ('B', 'X'): 'loss',
        ('B', 'Y'): 'draw' ,
        ('B', 'Z'): 'win',
        ('C', 'X'): 'win',
        ('C', 'Y'): 'loss' ,
        ('C', 'Z'): 'draw',
    }
    return outcome_dictionary[round_data]

def score_for_round(round_data: tuple[str, str]) -> int:
    score_for_shape_dictionary = {'X': 1, 'Y': 2, 'Z': 3}
    score_for_shape: int = score_for_shape_dictionary[round_data[1]]
    score_for_outcome_dictionary = {'loss': 0, 'draw': 3, 'win': 6}
    outcome: str = outcome_of_round(round_data=round_data)
    score_for_outcome: int = score_for_outcome_dictionary[outcome]
    return score_for_shape + score_for_outcome