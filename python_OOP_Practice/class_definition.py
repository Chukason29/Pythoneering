class Student:
    #TODO Add class variables

    #__init__ is used to assign  properties to objects created from this class or create instance variables
    def __init__(self, name: str, age: int, height: float): #always assign types to properties
        self.name = name
        self.age = age
        self.height = height
    
    #TODO write out static methods that belong only to classes
    #@staticmethod
    def staticMethod(params): #static methods do not require a self parameter 
        pass


    #TODO write out instance methods accessible by object(instance)
    #because instance methods are accessible from an object hence, self is needed
    def instanceMethod (self, params):
        pass


#Create objects from Students class
student1 = Student("Uche", 1.4, 6)
print (student1.name)
print (student1.age)
print (student1.height)


    