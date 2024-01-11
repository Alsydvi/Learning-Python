
import unittest
import leapyear

class Testing(unittest.TestCase):

    def test_leap_year_ad(self):
        year_result = main.is_leap_year_ad_num(2012)
        self.assertEqual(year_result, "Leap year!")

    def test_special_leap_year_ad(self):
        year_result = main.is_leap_year_ad_num(2000)
        self.assertEqual(year_result, "Leap year!")

    def test_not_leap_year_ad(self):
        year_result = main.is_leap_year_ad_num(2011)
        self.assertEqual(year_result, "Not a leap year :(")


    def test_leap_year_bc(self):
        year_result = main.is_leap_year_bc_num(-399)
        self.assertEqual(year_result, "Leap year!")

    def test_not_leap_year_bc(self):
        year_result = main.is_leap_year_bc_num(-400)
        self.assertEqual(year_result, "Not a leap year :(")

    def test_leap_year_bc(self):
        year_result = main.is_leap_year_bc_num(-8)
        self.assertEqual(year_result, "Leap year!")

   def test_not_leap_year_bc(self):
        year_result = main.is_leap_year_bc_num(-6)
        self.assertEqual(year_result, "Not a leap year :(")


if __name__ == '__main__':
    unittest.main()
