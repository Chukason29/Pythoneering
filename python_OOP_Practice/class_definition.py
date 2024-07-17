class Student:
    #__init__ is used to assign  properties to objects created from this class
    def __init__(self, name: str, age: int, height: float): #always assign 
        self.name = name
        self.age = age
        self.height = height

#Create objects from Students class

student1 = Student("Uche", 1.4, 6)
print(student1)
    