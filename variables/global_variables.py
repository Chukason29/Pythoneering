"""
global variables are variables that are defined outside the a function or a class

Note==> the redeclaration of a global variable in a function does not change the value of the global variable
"""

name = "Chukwuebuka" #global variable

def myName():
    name = "Victor" #local variable
    print(name)


print(name) #prints chukwuebuka 
myName() #prints victor