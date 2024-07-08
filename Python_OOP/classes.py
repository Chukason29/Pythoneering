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
student1 = Student("Tommyzan", 40) #The arguments reps the name and age in the __init__() of the student class
student2 = Student("Patricia", 25)

print(f"My name is  {student1.name} and I am {student1.age} years old")
print(f"My name is {student2.name}, I'm the second student for GGSS")