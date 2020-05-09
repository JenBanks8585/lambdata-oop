# lambdata-oop
## Steak N' Shake helpers with OOP
    This is a subset of Steak N' Shake menu that covers 
        a. Burgers
        b. Chili

    Intallation:
        pip install -i https://test.pypi.org/simple/ Order


    Chili Methods:
        a. chili_type(self)
            # function describing chili type, price and calories

        b. with_cheese(self)
            # function whether it has cheese or not

        c. with_pasta(self)
            # function whether it has pasta or not
    
    Burger Methods:
        a. apply_discount(self)
            # function where potential discount can be applied

        b. burger_type(self)
            # function describing burger type, price and calories

        c. with_lettuce(self)
           # function whether it has lettuce or no


## Example Instances:

### Chili Instances
   * c1 = Chili('Chili Mac', 4.49, 1200, True, False)
   * c2 = Chili('Chili Mac Supreme', 4.99, 1410, True, True)
   * c3 = Chili('Chili 3-Way', 4.99, 710, True, False)
   * c4 = Chili('Chili 5- Way', 4.99, 1160, True, True)
   * c5 = Chili('Genuine Chili', 4.99, 550, False, False)
   * c6 = Chili('Chili Deluxe', 4.99, 1000, False, False)

### Burger instances
   * b1 = Burger('Pork Belly Double', 6.49, 740, False)
   * b2 = Burger('Original Double n Cheese', 3.99, 770, True)
   * b3 = Burger('Single n Cheese', 3.79, 630, True)
   * b4 = Burger('Triple Steakburger n Fries', 3.99, 850, True)
  * b5 = Burger('Frisco Melt n Fries', 5.49, 1200, False)

## Sample results
  * print (b1.burger_type())
  * print (b1.with_lettuce())
  * print(b2.price)
  * print (b2.apply_discount())
  * print (Menu.num_of_products)
  * print (c1.chili_type())
  * print (c2.with_cheese())
  * print(c2.price)
  * print (c3.with_cheese())
