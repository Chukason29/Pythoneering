"""
Assertions are used to enforce the kind of data to be passed into any method in a class
"""
pupil = {
    "name": 32,
    "ca1" : 20,
    "ca2" : 16,
    "exam" : 50
}

#Inputting and collating a student' scores 
class Student:
    def __init__(self, name: str, ca1: int, ca2: int, exam: int): #always name each datatyp
        #Asserting values guides the input of data
        assert ca1 >=0 and ca1 <=20, f"CA1 shouldn't be more than 20 nor less than 0"
        assert ca2 >=0 and ca2 <=20,  f"CA2 shouldn't be more than 20 nor less than 0"
        assert exam >=0 and exam <=60, f"Exam shouldn't be more than 20 nor less than 0"
        #Instatiating Object Properties
        self.name = name
        self.ca1 = ca1
        self.ca2 = ca2
        self.exam = exam
    
    #This method returns the summation of ca1, ca2 and exam
    def sumGrades (self):
        return self.ca1 + self.ca2 + self.exam
    
studentScore = Student(pupil["name"], pupil["ca1"], pupil["ca2"], pupil["exam"])