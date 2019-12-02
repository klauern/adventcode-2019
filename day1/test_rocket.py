from unittest import TestCase

from day1.rocket import fuel


class Test(TestCase):

    def test_fuel_12(self):
        assert fuel(12) == 2

    def test_fuel_14(self):
        assert fuel(14) == 2

    def test_1969(self):
        assert fuel(1969) == 654

    def test_100756(self):
        assert fuel(100756) == 33583
