class Menu:

    """
## Steak N' Shake helpers with OOP
    This is a subset of Steak N' Shake menu that covers
        a. Burgers
        b. Chili

    Intallation:
        pip install -i https://test.pypi.org/simple/ Order

    Imports:
        from helper.menu import Burger, Chili, Menu


    Menu Methods:
        a. Add price of any two available items
           print(c1 + b2)

        b. Number of Products available
           print (Menu.num_of_products)

        c. Computes discounted price
           print (b2.apply_discount())
"""

    # class variables
    num_of_products = 0
    discount = 0.95

    def __init__(self, name, price, calory):
        self.name = name
        self.price = price
        self.calory = calory

        Menu.num_of_products += 1

    # dunder method to add any two available items' prices
    def __add__(self, other):
        return self.price + other.price


class Burger(Menu):

    """
class Burger inherits Menu attributes and class variables.

 Burger Methods:
    a. apply_discount(self)
        # function where potential discount can be applied

    b. burger_type(self)
        # function describing burger type, price and calories

    Sample results:
        print (b1.burger_type())
        print(b2.price)
        print(b2.name)
        print(b4.lettuce)
"""

    def __init__(self, name, price, calory, lettuce):
        super(). __init__(name, price, calory)
        self.lettuce = lettuce

    # function describing burger type, price and calories
    def burger_type(self):
        return '{} {} {} {} {}'. format(self.name, '$',
                                        self.price, self.calory, 'cal')

    # function where potential discount can be applied
    def apply_discount(self):
        self.price = float(self.price * self.discount)
        return '{} {}'. format('Discounted price is: $', self.price)

    # Function whether it has lettuce or not
    def with_lettuce(self):
      if self.lettuce is True:
        return "This burger has lettuce."
      else:
        return "This burger does not have lettuce."


class Chili(Menu):

    """
class Chili inherits Menu attributes and class variables.

Chili Methods:
    a. chili_type(self)
        # function describing chili type, price, calories, cheese content

    Sample results:
        print (c1.chili_type())
        print(c2.price)
        print(c2.name)
        print(c4.cheese)
  """

    def __init__(self, name, price, calory, cheese):
        super(). __init__(name, price, calory)
        self.cheese = cheese

    # function describing chili type, price and calories
    def chili_type(self):
        return '{} {} {} {} {}'. format(self.name,
                                        '$', self.price,
                                        self.calory, 'cal')

if __name__ == "__main__":

    def __add__(self, other):
        return self.price + other.price

""" #Chili Instances
  c1 = Chili('Chili Mac', 4.49, 1200, 'With Cheese')
  c2 = Chili('Chili Mac Supreme', 4.99, 1410, 'No Cheese')
  c3 = Chili('Chili 3-Way', 4.99, 710, 'With Cheese')
  c4 = Chili('Chili 5- Way', 4.99, 1160, 'With Cheese')
  c5 = Chili('Genuine Chili', 4.99, 550, 'No Cheese')
  c6 = Chili('Chili Deluxe', 4.99, 1000, 'With Cheese')

# Burger instances
  b1 = Burger('Pork Belly Double', 6.49, 740, True)
  b2 = Burger('Original Double n Cheese', 3.99, 770, True)
  b3 = Burger('Single n Cheese', 3.79, 630, False)
  b4 = Burger('Triple Steakburger n Fries', 3.99, 850, False)
  b5 = Burger('Frisco Melt n Fries', 5.49, 1200, True)


  # Sample results
  print (b1.burger_type())
  print(b2.price)
  print (b2.apply_discount())
  print (Menu.num_of_products)

  print (c1.chili_type())
  print(c2.price)
  print ('Price of two items is ' , c2 + b1)
  print (c2.cheese) """
