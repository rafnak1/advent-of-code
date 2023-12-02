import utils

def rock_paper_scissors_solve(raw_input: str) -> int:
    parsed_input: list[tuple[str, str]] = utils.parse_input(raw_input=raw_input)
    return sum( [utils.score_for_round(round_data=round_data) for round_data in parsed_input] )

if __name__ == "__main__":
    with open('input.txt') as f:
        raw_input = f.read()
    print(rock_paper_scissors_solve(raw_input=raw_input))
