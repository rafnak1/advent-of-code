import unittest, solution_part1

class TestRockPaperScissorsSolve(unittest.TestCase):

    def test_generic(self):
        raw_input = "A Y\nB X\nC Z\n"
        obtained: int = solution_part1.rock_paper_scissors_solve(raw_input=raw_input)
        self.assertEqual(obtained, 15)

class TestParseInput(unittest.TestCase):

    def test_generic(self):
        raw_input: str = "A X\nB X\nC Z\nB Z\n"
        obtained: list[tuple[str, str]] = solution_part1.parse_input(raw_input=raw_input)
        expected = [('A', 'X'), ('B', 'X'), ('C', 'Z'), ('B', 'Z')]
        self.assertEqual(obtained, expected)

class TestScoreForRound(unittest.TestCase):
    
    def test_A_Y(self):
        round_data: tuple[str, str] = ('A', 'Y')
        obtained: int = solution_part1.score_for_round(round_data=round_data)
        self.assertEqual(obtained, 8)

    def test_B_X(self):
        round_data: tuple[str, str] = ('B', 'X')
        obtained: int = solution_part1.score_for_round(round_data=round_data)
        self.assertEqual(obtained, 1)

    def test_C_Z(self):
        round_data: tuple[str, str] = ('C', 'Z')
        obtained: int = solution_part1.score_for_round(round_data=round_data)
        self.assertEqual(obtained, 6)

class TestOutcomeOfRound(unittest.TestCase):

    def test_A_Y(self):
        round_data: tuple[str, str] = ('A', 'Y')
        obtained: str = solution_part1.outcome_of_round(round_data=round_data)
        self.assertEqual(obtained, 'win')

    def test_B_X(self):
        round_data: tuple[str, str] = ('B', 'X')
        obtained: str = solution_part1.outcome_of_round(round_data=round_data)
        self.assertEqual(obtained, 'loss')

    def test_C_Z(self):
        round_data: tuple[str, str] = ('C', 'Z')
        obtained: str = solution_part1.outcome_of_round(round_data=round_data)
        self.assertEqual(obtained, 'draw')

if __name__ == '__main__':
    unittest.main()