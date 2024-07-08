"""
A class is the blueprint used in creating objects
A class has basically three parts

==> Constructor
==> Properties
==> Methods
"""

class Student:
    def __init__(self, name, age): # This is a constructor function, it is used to a
        self.name = name
        self.age = age

#creating sn object
newStudent = Student("Tommyzan", 40) #The arguments reps the name and age in the __init__() of the student class

print(f"My name is  {newStudent.name} and I am {newStudent.age} years old")
