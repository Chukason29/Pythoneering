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

    #TODO declare instance variables

    #TODO write a method the cuts product price by 30% using class variable
    pass

#TODO 







