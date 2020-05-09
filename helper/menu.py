

class Menu:

    # class variables
    num_of_products = 0
    discount = 0.95

    def __init__(self, name, price, calory):
        self.name = name
        self.price = price
        self.calory = calory

        Menu.num_of_products += 1