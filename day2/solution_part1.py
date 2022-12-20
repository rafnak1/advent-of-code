def rock_paper_scissors_solve(raw_input: str) -> int:
    return 0

def parse_input(raw_input: str) -> list[tuple[str, str]]:
    stripped_input: str = raw_input.strip()
    newline_split_input: list[str] = stripped_input.splitlines()
    parsed_input: list[tuple[str, str]] = [(line[0], line[2]) for line in newline_split_input]
    return parsed_input