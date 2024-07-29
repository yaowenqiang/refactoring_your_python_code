import unittest

from session_FizzBuzz import fizzbuzz

class FizzBuzzTests(unittest.TestCase):
    def test_for_1(self):
        self.assertEqual(fizzbuzz(1), 1)

    def test_for_2(self):
        self.assertEqual(fizzbuzz(2), 2)


if __name__ == '__main__':
    unittest.main()