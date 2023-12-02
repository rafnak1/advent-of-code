import unittest, utils, solution_part1, solution_part2

class TestPart1RockPaperScissorsSolve(unittest.TestCase):

    def test_generic(self):
        raw_input = "A Y\nB X\nC Z\n"
        obtained: int = solution_part1.rock_paper_scissors_solve(raw_input=raw_input)
        self.assertEqual(obtained, 15)

class TestParseInput(unittest.TestCase):

    def test_generic(self):
        raw_input: str = "A X\nB X\nC Z\nB Z\n"
        obtained: list[tuple[str, str]] = utils.parse_input(raw_input=raw_input)
        expected = [('A', 'X'), ('B', 'X'), ('C', 'Z'), ('B', 'Z')]
        self.assertEqual(obtained, expected)

class TestScoreForRound(unittest.TestCase):
    
    def test_A_Y(self):
        round_data: tuple[str, str] = ('A', 'Y')
        obtained: int = utils.score_for_round(round_data=round_data)
        self.assertEqual(obtained, 8)

    def test_B_X(self):
        round_data: tuple[str, str] = ('B', 'X')
        obtained: int = utils.score_for_round(round_data=round_data)
        self.assertEqual(obtained, 1)

    def test_C_Z(self):
        round_data: tuple[str, str] = ('C', 'Z')
        obtained: int = utils.score_for_round(round_data=round_data)
        self.assertEqual(obtained, 6)

class TestOutcomeOfRound(unittest.TestCase):

    def test_A_Y(self):
        round_data: tuple[str, str] = ('A', 'Y')
        obtained: str = utils.outcome_of_round(round_data=round_data)
        self.assertEqual(obtained, 'win')

    def test_B_X(self):
        round_data: tuple[str, str] = ('B', 'X')
        obtained: str = utils.outcome_of_round(round_data=round_data)
        self.assertEqual(obtained, 'loss')

    def test_C_Z(self):
        round_data: tuple[str, str] = ('C', 'Z')
        obtained: str = utils.outcome_of_round(round_data=round_data)
        self.assertEqual(obtained, 'draw')

class TestTranslateRoundData(unittest.TestCase):
    
    def test_A_Y(self):
        round_data: tuple[str, str] = ('A', 'Y')
        obtained: tuple[str, str] = solution_part2.translate_round_data(round_data=round_data)
        self.assertEqual(obtained, ('A', 'X'))

    def test_B_X(self):
        round_data: tuple[str, str] = ('B', 'X')
        obtained: tuple[str, str] = solution_part2.translate_round_data(round_data=round_data)
        self.assertEqual(obtained, ('B', 'X'))

    def test_C_Z(self):
        round_data: tuple[str, str] = ('C', 'Z')
        obtained: tuple[str, str] = solution_part2.translate_round_data(round_data=round_data)
        self.assertEqual(obtained, ('C', 'X'))

class TestPart2RockPaperScissorsSolve(unittest.TestCase):

    def test_generic(self):
        raw_input = "A Y\nB X\nC Z\n"
        obtained: int = solution_part2.rock_paper_scissors_solve(raw_input=raw_input)
        self.assertEqual(obtained, 12)

if __name__ == '__main__':
    unittest.main()