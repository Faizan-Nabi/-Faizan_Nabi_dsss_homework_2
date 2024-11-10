import unittest
from math_quiz import get_random_integer, get_random_operator, calculate_answer


class TestMathGame(unittest.TestCase):

    def test_get_random_integer(self):
        # Testing if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Tested a large number of random values
            rand_num = get_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_operator(self):
        # Testing if the function returns one of the allowed operators
        allowed_operators = ['+', '-', '*']
        for _ in range(100):  # Test a large number of random choices
            operator = get_random_operator()
            self.assertIn(operator, allowed_operators)

    def test_calculate_answer(self):
        # Testing cases for addition, subtraction, and multiplication
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (7, 3, '-', '7 - 3', 4),
            (6, 4, '*', '6 * 4', 24)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = calculate_answer(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
