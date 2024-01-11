
import unittest
import LeapYear

class Testing(unittest.TestCase):

    def test_leap_year_ad(self):
        year_result = LeapYear.is_leap_year_ad_num("2012")
        self.assertEqual(year_result, "Leap year!")

    def test_special_leap_year_ad(self):
        year_result = LeapYear.is_leap_year_ad_num("2000AD")
        self.assertEqual(year_result, "Leap year!")

    def test_not_leap_year_ad(self):
        year_result = LeapYear.is_leap_year_ad_num("2011")
        self.assertEqual(year_result, "Not a leap year :(")


    def test_leap_year_bc(self):
        year_result = LeapYear.is_leap_year_bc_num("399bC")
        self.assertEqual(year_result, "Not a leap year :(")

    def test_not_leap_year_bc(self):
        year_result = LeapYear.is_leap_year_bc_num("400BC")
        self.assertEqual(year_result, "Not a leap year :(")

    def test_leap_year_bc(self):
        year_result = LeapYear.is_leap_year_bc_num("9bc")
        self.assertEqual(year_result, "Leap year!")

    def test_not_leap_year_bc(self):
        year_result = LeapYear.is_leap_year_bc_num("6Bc")
        self.assertEqual(year_result, "Not a leap year :(")


if __name__ == '__main__':
    unittest.main()
