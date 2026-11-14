# https://github.com/DWebb-77/lab11-DW-LL.git
# Partner 1: Dylan Webb
# Partner 2: Lucas Lyle

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-4, 1), -3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(-2, -2), 0)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(7, 6), 42)
        self.assertEqual(mul(2, 0), 0)
        self.assertEqual(mul(2, 10), 20)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 10,), 5)
        self.assertEqual(div(1, 1), 1)
        self.assertEqual(div(3, 0,), 0)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(3, 1), 0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-2, 8)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(2, 4), 5)
        self.assertEqual(hypotenuse(9, 40), 41)
        self.assertEqual(hypotenuse(15, 8), 17)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-3)
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(100), 10)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()