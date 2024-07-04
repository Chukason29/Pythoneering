"""
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.

Number of Arguments
By default, a function must be called with the correct number of arguments. Meaning that if your 
function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
"""
def addNums(a, b):
    return a + b

print(addNums(2,3))

def fullName(fname, lname):
    print(fname)

#fullName("Ebuka") #this will cause an error because we used only one argument when two parameters were 

#Keyword Arguments
def student(studentName, studentClass):
    print(f"My name is {studentName} and I am in {studentClass}")
student(studentName="Chukwuebuka", studentClass= "JSS 2")

