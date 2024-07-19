import csv

class Student:
    #creating a list to store all instances
    all_instances = []

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

        Student.all_instances.append(self) #appends all instances to a list

    #TODO using class methods to automatically instantiate objects from a database
    @classmethod #==> always use decorators
    def instantiate_objects(cls): #what self is to instance methods is what cls is to class methods
        #reading data from a csv file and converting to a list
        with open('C:/Users/USER/Desktop/Pythoneering/python_OOP_Practice/data.csv', 'r') as f:
            reader = csv.DictReader(f)
            students = list(reader)
        
        for student in students:
            #creating an instance for each record on the
            Student(
                name = student.get("name"),
                age = student.get("age"),
                height = student.get("height")
            )
    def __repr__(self):
        return f"Student({self.name}, {self.age}, {self.height})"
        pass
Student.instantiate_objects()
print(Student.all_instances)