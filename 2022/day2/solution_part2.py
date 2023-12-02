import utils

def translate_round_data(round_data: tuple[str, str]) -> tuple[str, str]:
    outcome_dictionary = {
        'X': 'loss',
        'Y': 'draw',
        'Z': 'win'
    }
    intended_play_dictionary = {
        ('A', 'draw'): 'X',
        ('A', 'win'): 'Y' ,
        ('A', 'loss'): 'Z',
        ('B', 'loss'): 'X',
        ('B', 'draw'): 'Y' ,
        ('B', 'win'): 'Z',
        ('C', 'win'): 'X',
        ('C', 'loss'): 'Y' ,
        ('C', 'draw'): 'Z',
    }
    intended_move = intended_play_dictionary[ (round_data[0], outcome_dictionary[round_data[1]]) ]
    return (round_data[0], intended_move)


def rock_paper_scissors_solve(raw_input: str) -> int:
    parsed_input: list[tuple[str, str]] = utils.parse_input(raw_input=raw_input)
    translated_game_data: list[tuple[str, str]] = [translate_round_data(round_data) for round_data in parsed_input]
    return sum( [utils.score_for_round(round_data=round_data) for round_data in translated_game_data] )

if __name__ == "__main__":
    with open('input.txt') as f:
        raw_input = f.read()
    print(rock_paper_scissors_solve(raw_input=raw_input))
