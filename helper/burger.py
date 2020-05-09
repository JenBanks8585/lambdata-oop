from menu import *


class Burger(Menu):

    def __init__(self, name, price, calory, lettuce):
        super(). __init__(name, price, calory)

    # function describing burger type, price and calories
    def burger_type(self):
        return '{} {} {} {} {}'. format(self.name,
                                        '$', self.price, 
                                        self.calory, 'cal')

    # function whether it has lettuce or not  
    def with_lettuce(self):
        self.lettuce = True
        if True:
            return "This burger has lettuce"
        else:
            return "This burger does NOT have lettuce"

    # function where potential discount can be applied
    def apply_discount(self):
        self.price= float(self.price * self.discount)
        return '{} {}'. format('Discounted price is: $', self.price) 
    
# Burger instances
b1 = Burger('Pork Belly Double', 6.49, 740, False)
b2 = Burger('Original Double n Cheese', 3.99, 770, True)
b3 = Burger('Single n Cheese', 3.79, 630, True)
b4 = Burger('Triple Steakburger n Fries', 3.99, 850, True)
b5 = Burger('Frisco Melt n Fries', 5.49, 1200, False)

# Sample results
print (b1.burger_type())
print (b3.with_lettuce())
print(b2.price)
print (b2.apply_discount())
print (Menu.num_of_products)
