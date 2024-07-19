import csv

class Student:
    #creating a list to store all instances
    all_instances = []

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Student.all_instances.append(self) #appends all instances to a "all_instances" list

    @classmethod
    #This method creates objects
    def current_object(cls): 
        with open('C:/Users/USER/Desktop/Pythoneering/python_OOP_Practice/data.csv', 'r') as f:
            reader = csv.DictReader(f)
            students = list(reader)
            for student in students:
                if int(student["age"]) <= 20:
                    Student(
                        name = student["name"],
                        age = int(student["age"]),
                        height = float(student["height"])
                    )
    def __repr__(self):
        return f"Student({self.name}, {self.age}, {self.height})"
        pass
#Student.instantiate_objects()
Student.current_object()
print(Student.all_instances)
