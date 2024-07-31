# 1000, M
# 500, D
# 100, C
# 50, L
# 10, X
# 5, V
# 1, I

import unittest

def convert(number):
    if number == 2:
        return 'II'
    if number == 1:
        return 'I'

class RomanNumeralsTest(unittest.TestCase):
    def test_for_1(self):
        self.assertEqual(convert(1), 'I')

    def test_for_2(self):
        self.assertEqual(convert(2), 'II')

    def test_4(self):
        self.assertEqual(convert(4), 'IV')

    def test_5(self):
        self.assertEqual(convert(5), 'V')

    def test_9(self):
        self.assertEqual(convert(9), 'IX')

if __name__ == '__main__':
    unittest.main()