"""
Items can be removed from the list
"""

fruits = ["Apple", "Mango", "Orange", "Apricot", "Guavas", "Cherry", "Watermelon", "Pineapple", "Apricot"]

#.remove(), removes the specified item

if "Apricot" in fruits:
    fruits.remove("Apricot")# removes apricot from the system
    print(fruits)
else:
    print("Apricot is not found in the system")

#If there are two apricots found it removes only the firs occurence found.