"""
There are two kinds of attributes in OOP

1==> Instance Attributes
2==> Class Attributes
"""

#Instance Attributes are attributes that are declared within __init__()
#And are instatiated during creating the objects

class Player:
    #These are instance variables 
    def __init__(self, name, goals, stats):
        self.name = name
        self.goals = goals
        self.stats = stats

#Class variables are only useful within the class.
#They are defined outside any method instead are declared directly under the class itself

#Use of class and instance variables in product pricing
class Product:
    #TODO: Declare class variables
    priceCut = 0.7 #this is a class variable

    #TODO declare instance variables
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category

    #TODO write a method the cuts product price by 30% using class variable
    def priceRate(self):
        return self.price * self.priceCut

#TODO instantiate product1 ==> Product 1 should have a price cut of 50%
product1 = Product("Phone", 1000.00, "Electronics")
print(product1.priceRate())


#TODO instantiate product2 ==> Product 1 should have a price cut of 50%
product2 = Product("Shoe", 500.00, "Fashion")
product2.priceCut = 0.5
print(product2.priceRate())


#NOTE==>  Every object checks for properties first from its instance variebles, then before checking for class variables




