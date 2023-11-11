import unittest
from math_quiz import generate_random_integer, generate_random_operator, calculate_result


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        # TODO
        # Test if random operator generated is one of the specified operators
        operators = {'+', '-', '*'}
        for _ in range(1000):  # Test a large number of random values
            rand_operator = generate_random_operator()
            self.assertIn(rand_operator, operators)

    def test_calculate_result(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (3, 4, '-', '3 - 4', -1),
                (2, 6, '*', '2 * 6', 12),
                # Add more test cases as needed
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                result = calculate_result(num1, num2, operator)
                self.assertEqual(result, expected_answer)

                # Check if the problem string is formatted correctly
                problem, _ = calculate_result(num1, num2, operator)
                self.assertEqual(problem, expected_problem)

if __name__ == "__main__":
    unittest.main()
