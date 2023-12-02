import utils, solution_part1, solution_part2, unittest

class TestParseInput(unittest.TestCase):

    def test_parse_input(self):
        with open("test_input.txt") as f:
            raw_input = f.read()

        obtained: list[list[int]] = utils.parse_input(raw_input=raw_input)

        expected = [[5,20,30], [20,30], [60]]
        self.assertEqual(obtained, expected)

class TestMaximumAmountOfCaloriesInOneInventory(unittest.TestCase):

    def test_maximum_amount_of_calories_in_one_inventory(self):
        example_input = [[1000,2000,3000], [4000], [5000,6000], [7000,8000,9000], [10000]]

        obtained = solution_part1.maximum_amount_of_calories_in_one_inventory(example_input)

        self.assertEqual(obtained, 24000)

class TestSumOfTop3ElfCalories(unittest.TestCase):

    def test_sum_of_top_3_elf_calories(self):
        example_input = [[1000,2000,3000], [4000], [5000,6000], [7000,8000,9000], [10000]]

        obtained = solution_part2.sum_of_top_3_elf_calories(example_input)

        self.assertEqual(obtained, 45000)

if __name__ == '__main__':
    unittest.main()