# 1000, M
# 500, D
# 100, C
# 50, L
# 10, X
# 5, V
# 1, I

import unittest

def convert(number):
    roman = ''
    arabic_numerals = [50, 10, 5, 1]
    roman_numerals = ['L', 'X', 'V', 'I']
    for i in range(len(arabic_numerals)):
        while number >= arabic_numerals[i]:
            roman += roman_numerals[i]
            number -= arabic_numerals[i]
    return roman
def convert2(number):
    roman = ''
    arabic_numerals = [ 10, 1]
    roman_numerals = ['X', 'I']
    while number >= arabic_numerals[0]:
        roman += roman_numerals[0]
        number -= arabic_numerals[0]

    while number >= arabic_numerals[1]:
        roman += roman_numerals[1]
        number -= arabic_numerals[1]
    return roman

def convert_2(number):
    arabic_numeral = 10
    roman = ''
    roman_numeral = 'X'
    while number >= arabic_numeral:
        roman += roman_numeral
        number -= arabic_numeral

    arabic_numeral = 1
    roman_numeral = 'I'
    while number >= arabic_numeral:
        roman += roman_numeral
        number -= arabic_numeral

    # for _ in range(number):
    #     roman += 'I'
    # if number == 3:
    #     roman =  'III'
    # if number == 2:
    #     roman =  'II'
    # if number == 1:
    #     roman = 'I'
    return roman

class RomanNumeralsTest(unittest.TestCase):
    def test_for_1(self):
        self.assertEqual(convert(1), 'I')

    def test_for_2(self):
        self.assertEqual(convert(2), 'II')

    def test_for_3(self):
        self.assertEqual(convert(3), 'III')

    def test_4(self):
        self.assertEqual(convert(4), 'IV')

    def test_5(self):
        self.assertEqual(convert(5), 'V')

    def test_9(self):
        self.assertEqual(convert(9), 'IX')

    def test_10(self):
        self.assertEqual(convert(10), 'X')

    def test_20(self):
        self.assertEqual(convert(20), 'XX')

    def test_30(self):
        self.assertEqual(convert(30), 'XXX')

    def test_50(self):
        self.assertEqual(convert(50), 'L')

if __name__ == '__main__':
    unittest.main()