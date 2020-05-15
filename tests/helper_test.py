import unittest

from from helper.menu import Burger, Chili

class HelperTestMethod(unittest.TestCase):

    def test_apply_discount(self):
        self.assertEqual(apply_discount(4, .9), 3.6)

        with self.assertRaises(TypeError):
            apply_discount(4, 2), 3.6)




        # function where potential discount can be applied
    def apply_discount(self):
        self.price = float(self.price * self.discount)
        return '{} {}'. format('Discounted price is: $', self.price)








    def test_add_state_names_oop(self):
        # expect that it has one more column and the same number of rows, after we invoke the function
        # expect that certain column names exist before and certain col names exist after
        df = DataFrame({"abbrev":["CA","CO","CT","DC","TX"]})
        processor = DataProcessor(df)
        self.assertEqual(list(processor.df.columns), ['abbrev'])
        processor.add_state_names()
        self.assertEqual(list(processor.df.columns), ["abbrev", "name"])
        self.assertEqual(processor.df.iloc[0]["abbrev"], "CA")
        self.assertEqual(processor.df.iloc[0]["name"], "Cali")
if __name__ == "__main__":
    unittest.main()