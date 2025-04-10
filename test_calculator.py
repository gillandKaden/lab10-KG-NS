# https://github.com/gillandKaden/lab10-KG-NS
# Partner 1: Kaden Gilland
# Partner 2: Nicholas Simeone
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
        pass

    def test_subtract(self): # 3 assertions
        pass
    ##########################

    # Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(50,5),250)
        self.assertEqual(mul(111,0),0)
        self.assertEqual(mul(22,-1),-22)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(55,5),11)
        self.assertEqual(div(63,-7),-9)

    ##########################

    # Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        pass

    def test_logarithm(self): # 3 assertions
        pass

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        pass
    ##########################
    
    # Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        with self.assertRaises(ValueError):
             logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-20)
        self.assertEqual(square_root(16),4)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()