"""
Items can be added to sets using .add()
"""

fruits = {"Apple", "Mango", "Orange", "Apricot", "Guavas", "Cherry", "Watermelon", "Pineapple", "Apricot", "3Maple"}
fruits.add("Grape")
print(fruits) #Grape is added

#Adding a whole list or set to another set

fruities = {"Avocado", "Lemon", "Lime"}

fruits.update(fruities)
print(fruits)

fruitList = list(fruities)

fruitList[0] = "Guava"
print(fruitList)

fruities = set(fruitList)
print(fruities)