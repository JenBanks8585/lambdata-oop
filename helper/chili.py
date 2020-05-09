""" from menu import Menu


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

#Chili Instances
c1 = Chili('Chili Mac', 4.49, 1200, True, False)
c2 = Chili('Chili Mac Supreme', 4.99, 1410, True, True)
c3 = Chili('Chili 3-Way', 4.99, 710, True, False)
c4 = Chili('Chili 5- Way', 4.99, 1160, True, True)
c5 = Chili('Genuine Chili', 4.99, 550, False, False)
c6 = Chili('Chili Deluxe', 4.99, 1000, False, False)

# Sample results
print (c1.chili_type())
print (c2.with_cheese())
print(c2.price)
print (Menu.num_of_products)
print (c3.with_cheese()) """