import unittest

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):

    def test_fun(self):
        weekday = calculate(2001, 1, 3)
        self.assertEqual(weekday, 2005)

        retcode = main(("--year", "2001", "--month", "1", "--day", "3"))
        self.assertEqual(retcode, 0)

        retcode1 = main(("--ar", "2001", "--month", "1", "--day", "3"))
        self.assertNotEqual(retcode1, 1)

        retcode2 = main(("--year", 2001, "--month", "1", "--day", "3"))
        self.assertNotEqual(retcode2, 1)

        retcode3 = main(("--year", "2001", "--month", "1,2,3", "--day", "3"))
        self.assertNotEqual(retcode3, 1)

        retcode4 = main(("--year", "2001-22", "--month", "1", "--day", "3"))
        self.assertNotEqual(retcode4, 1)

        retcode5 = main(("--year", "2001", "--th", "1", "--day", "3"))
        self.assertNotEqual(retcode5, 1)

        retcode6 = main(("--year", "2001", "--month", "1", "--day", "mama"))
        self.assertNotEqual(retcode6, 1)

        retcode7 = main(("--year", "2001", "--month", "marzec", "--day", "3"))
        self.assertNotEqual(retcode7, 1)

    def test_calculate(self):

        weekday = calculate(2001-200, 1, 3)
        self.assertEqual(weekday, None)

        monday = calculate(2017, 4, 10)
        self.assertEquals(monday, 0)

        weekend = calculate(2000, 13, 3)
        self.assertEquals(weekend, None)

        notday = calculate(2005, 2, 45)
        self.assertEquals(notday, None)

        friday = calculate(2016, 12, 9)
        self.assertEquals(friday, 4)












if __name__ == '__main__':
    unittest.main()
