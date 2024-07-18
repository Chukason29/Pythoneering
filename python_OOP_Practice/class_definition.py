class Student:
    #TODO Add class variables
    admin = "Chukwuebuka"

    #__init__ is used to assign  properties to objects created from this class or create instance variables
    def __init__(self, name: str, age: int, height: float): #always assign types to properties
        self.name = name
        self.age = age
        self.height = height
    
    #TODO assert keyword is used to control the kind or range of data
    #assert ca1 >=0 and ca1 <=20, f"CA1 shouldn't be more than 20 nor less than 0"
    #assert ca2 >=0 and ca2 <=20,  f"CA2 shouldn't be more than 20 nor less than 0" 
    
    #TODO write out static methods that belong only to classes
    #@staticmethod
    def staticMethod(params): #static methods do not require a self parameter 
        pass


    #TODO write out instance methods accessible by object(instance)
    #because instance methods are accessible from an object hence, self is needed
    def instanceMethod (self, params):
        pass
    
    def adminMethod():
        newAdmin = Student.admin #Accessing class variables

#Create objects from Students class
student1 = Student("Uche", 1.4, 6)

    