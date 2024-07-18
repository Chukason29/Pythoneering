class Student:
    #TODO Add class variables
    admin = "Chukwuebuka"

    #This list is used to store all instances as they are created
    allInstance = []
    #__init__ is used to assign  properties to objects created from this class or create instance variables
    def __init__(self, name: str, age: int, height: float): #always assign types to properties
        #TODO assert keyword is used to control the kind or range of data e.g no -ve values
        #assert ca1 >=0 and ca1 <=20, f"CA1 shouldn't be more than 20 nor less than 0"
        #assert ca2 >=0 and ca2 <=20,  f"CA2 shouldn't be more than 20 nor less than 0"
        self.name = name
        self.age = age
        self.height = height

        Student.allInstance.append(self) #with this all instances/objects are appended to the list at the time of creation
    
    #TODO write out static methods that belong only to classes
    @staticmethod
    def staticMethod(params): #static methods do not require a self parameter 
        pass

    #TODO class methods are methods that can only be access by the class itself not by an instance
    #e.g is the method used in creating objects for a class
    @classmethod #==> always use decorators
    def instantiate_objects(cls): #what self is to instance methods is what cls is to class methods
        pass


    #TODO write out instance methods accessible by object(instance)
    #because instance methods are accessible from an object hence, self is needed
    def instanceMethod (self, params):
        pass
    
    def adminMethod():
        newAdmin = Student.admin #Accessing class variables
    
    def __repr__(self): # magic method is needed when trying to show all the instances in allInstance list
        return f"Student({self.name}, {self.age}, {self.height})"

#Create objects from Students class
student1 = Student("Uche", 2.4, 6)
student1 = Student("Dera", 3.4, 7)
student1 = Student("Ebuks", 4.4, 8)
student1 = Student("Amy", 5.4, 9)
student1 = Student("Chybuz", 6.4, 10)   

print(Student.allInstance)