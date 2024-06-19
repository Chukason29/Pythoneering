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


#.pop() removes item from a particular index
fruits.pop(3)
print(fruits)

#.del() deletes the list completely or delete a specified index
#del fruits #deletes the fruits list

#.clear() clears all the items from the list

fruits.clear()
print(fruits) #prints an epmty list