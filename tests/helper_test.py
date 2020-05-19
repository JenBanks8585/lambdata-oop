import unittest

from helper.menu import Burger, Chili, Menu

class HelperTestMethod(unittest.TestCase):

    def test_apply_discount(self):
        b2 = Burger('Original Double n Cheese', 3.99, 770, True)
        self.assertEqual(b2.apply_discount(), f'Discounted price is: $ {3.7905}')

    def test_with_lettuce(self):
        b2 = Burger('Original Double n Cheese', 3.99, 770, True)
        self.assertEqual(b2.with_lettuce(), "This burger has lettuce")


if __name__ == '__main__':
    unittest.main()
