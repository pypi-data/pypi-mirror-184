import unittest
from src.ori_math_func import math_funcs


class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(math_funcs.add(5, 4), 9)
        self.assertEqual(math_funcs.add(7, 3), 10)
        self.assertEqual(math_funcs.add(5, -5), 0)

    def test_sub(self):
        self.assertEqual(math_funcs.sub(5, 5), 0)
        self.assertEqual(math_funcs.sub(10, 6), 4)
        self.assertEqual(math_funcs.sub(2, 5), -3)

    def test_multiply(self):
        self.assertEqual(math_funcs.multiply(5, 5), 25)
        self.assertEqual(math_funcs.multiply(5, 1), 5)
        self.assertEqual(math_funcs.multiply(4, 2), 8)
        self.assertEqual(math_funcs.multiply(4, -5), -20)

    def test_divide(self):
        self.assertEqual(math_funcs.divide(5, 5), 1)
        self.assertEqual(math_funcs.divide(5, -5), -1)
        self.assertEqual(math_funcs.divide(25, 5), 5)
        self.assertEqual(math_funcs.divide(5, 1), 5)
        self.assertEqual(math_funcs.divide(21, 7), 3)


if __name__ == '__main__':
    unittest.main()
