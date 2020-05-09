"""
class Menu 
        name, price, calory
"""

class Menu:

    # class variables
    num_of_products = 0
    discount = 0.95

    def __init__(self, name, price, calory):
        self.name = name
        self.price = price
        self.calory = calory

        Menu.num_of_products += 1

"""
class Burger inherits Menu attributes and class variables.
"""

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

"""
class Chili inherits Menu attributes and class variables.
"""

class Chili(Menu):
        
    def __init__(self, name, price, calory, pasta, cheese):
        super(). __init__(name, price, calory)

    # function describing chili type, price and calories
    def chili_type(self):
        return '{} {} {} {} {}'. format(self.name,
                                        '$', self.price, 
                                        self.calory, 'cal')
            
    # function whether it has cheese or not  
    def with_cheese(self):
        self.cheese = True
        if True:
            return "This chili has cheese"
        else:
            return "This chili does NOT have cheese"
    
    # function whether it has pasta or not  
    def with_pasta(self):
        self.pasta = True
        if True:
            return "This chili has pasta"
        else:
            return "This chili does NOT have pasta"

"""
#Chili Instances
c1 = Chili('Chili Mac', 4.49, 1200, True, False)
c2 = Chili('Chili Mac Supreme', 4.99, 1410, True, True)
c3 = Chili('Chili 3-Way', 4.99, 710, True, False)
c4 = Chili('Chili 5- Way', 4.99, 1160, True, True)
c5 = Chili('Genuine Chili', 4.99, 550, False, False)
c6 = Chili('Chili Deluxe', 4.99, 1000, False, False)

# Burger instances
b1 = Burger('Pork Belly Double', 6.49, 740, False)
b2 = Burger('Original Double n Cheese', 3.99, 770, True)
b3 = Burger('Single n Cheese', 3.79, 630, True)
b4 = Burger('Triple Steakburger n Fries', 3.99, 850, True)
b5 = Burger('Frisco Melt n Fries', 5.49, 1200, False)

# Sample results
print (b1.burger_type())
print (b1.with_lettuce())
print(b2.price)
print (b2.apply_discount())
print (Menu.num_of_products)

print (c1.chili_type())
print (c2.with_cheese())
print(c2.price)
print (c3.with_cheese())
"""