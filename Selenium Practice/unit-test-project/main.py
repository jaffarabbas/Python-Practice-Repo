import unittest
import calc

class TestCalculater(unittest.TestCase):
    def test_add(self):
        self.assertEqual((calc.add()), 15)

    # def test_subtract(self):
    #     self.assertEqual(calc.subtract(10, 5), 5)
    #     self.assertEqual(calc.subtract(-1, 1), -2)
    #     self.assertEqual(calc.subtract(-1, -1), 0)

    # def test_multiply(self):
    #     self.assertEqual(calc.multiply(10, 5), 50)
    #     self.assertEqual(calc.multiply(-1, 1), -1)
    #     self.assertEqual(calc.multiply(-1, -1), 1)
    #
    # def test_divide(self):
    #     self.assertEqual(calc.divide(10, 5), 2)
    #     self.assertEqual(calc.divide(-1, 1), -1)
    #     self.assertEqual(calc.divide(-1, -1), 1)
    #     self.assertEqual(calc.divide(5, 2), 2.5)
    #     self.assertEqual(calc.divide(5, 0), 'Cannot divide by zero')
    #

if __name__ == '__main__':
    unittest.main()