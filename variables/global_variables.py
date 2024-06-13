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


# You can use the global keyword to make a local variable global

def number():
    global num1
    num1 = 5

print(num1 + 4) #prints 9
