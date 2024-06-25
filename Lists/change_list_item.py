"""
Items in a list can be changed individually or collectively
"""

fruits = ["Apple", "Mango", "Orange", "Apricot", "Guavas", "Cherry"]

fruits[3] = "Berry"
print(fruits) # Berry will replace apricot

#replace the fourth and fifth item on the list
fruits[3:5] = ("Banana", "Watermelon")
print(fruits, len(fruits))

#replacing a single item with two new items
fruits[1:2] = ["Pineapple", "Plum"]
print(fruits, len(fruits)) # the length of the list will increase

#replacing multiple items and replace with a single item
fruits[0:2] = ("Udara")
print(fruits, len(fruits))