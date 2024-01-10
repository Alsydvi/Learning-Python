import unittest
import main

class Testing(unittest.TestCase):

    def test_leap_year(self):
        year_result = main.is_leap_year(2012)
        self.assertEqual(year_result, "Leap year!")

    def test_special_leap_year(self):
        year_result = main.is_leap_year(2000)
        self.assertEqual(year_result, "Leap year!")

    def test_not_leap_year(self):
        year_result = main.is_leap_year(2011)
        self.assertEqual(year_result, "Not a leap year :(")


if __name__ == '__main__':
    unittest.main()
