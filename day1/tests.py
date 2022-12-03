import solution, unittest

class TestParseInput(unittest.TestCase):

    def test_parse_input(self):
        with open("test_input.txt") as f:
            raw_input = f.read()

        obtained: list[list[int]] = solution.parse_input(raw_input=raw_input)

        expected = [[5,20,30], [20,30], [60]]
        self.assertEqual(obtained, expected)


if __name__ == '__main__':
    unittest.main()