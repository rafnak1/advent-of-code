import unittest, solution_part1

class TestRockPaperScissorsSolve(unittest.TestCase):

    @unittest.skip
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

if __name__ == '__main__':
    unittest.main()