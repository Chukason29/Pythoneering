"""
Sets cannot be accessed using index values
They are only accessed using loops
"""

fruits = {"Apple", "Mango", "Orange", "Apricot", "Guavas", "Cherry", "Watermelon", "Pineapple", "Apricot", "3Maple"}


#Looping Through a set
k = 1
for i in fruits:
    print(f"fruit {k} ==> {i}")
    k = k+1 

#Checking if item exists in set
myFruit = "Apricots"
if myFruit in fruits:
    print(f"{myFruit} is found")
else:
    print(f"{myFruit} is not found")