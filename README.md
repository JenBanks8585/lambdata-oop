# lambdata-oop
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
          
    
    Chili Methods:
        a. chili_type(self)
            # function describing chili type, price, calories with or without cheese

    Burger Methods:
        a. apply_discount(self)
            # function where potential discount can be applied

        b. burger_type(self)
            # function describing burger type, price, calories, with or without lettuce

        
## Example Instances:

### Chili Instances
   * c1 = Chili('Chili Mac', 4.49, 1200, 'With Cheese')
   * c2 = Chili('Chili Mac Supreme', 4.99, 1410, 'No Cheese')
   * c3 = Chili('Chili 3-Way', 4.99, 710, 'With Cheese')
   * c4 = Chili('Chili 5- Way', 4.99, 1160, 'With Cheese')
   * c5 = Chili('Genuine Chili', 4.99, 550, 'No Cheese')
   * c6 = Chili('Chili Deluxe', 4.99, 1000, 'With Cheese')

### Burger instances
   * b1 = Burger('Pork Belly Double', 6.49, 740, 'With Lettuce')
   * b2 = Burger('Original Double n Cheese', 3.99, 770, 'With Lettuce')
   * b3 = Burger('Single n Cheese', 3.79, 630, 'No Lettuce')
   * b4 = Burger('Triple Steakburger n Fries', 3.99, 850, 'No Lettuce')
   * b5 = Burger('Frisco Melt n Fries', 5.49, 1200, 'With Lettuce')

## Sample results
  * print (b1.burger_type())
  * print(b2.price)
  * print (b2.apply_discount())
  * print (Menu.num_of_products)

  * print (c1.chili_type())
  * print(c2.price)
  * print ('Price of two items is ' , c2 + b1)
  * print (c2.cheese)
