"""
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

Duplicates Not Allowed

The best way to remove duplicates from a list or tuple, is to just convert them to sets
"""
# Set declaration
set1 = {}
set2 = set()

print(type(set1))
print(type(set2))

#unordered ===> Means each item does not have definite position in the set, the position of an item can change anytime the set is being used
fruits = {"Apple", "Mango", "Orange", "Apricot", "Guavas", "Cherry", "Watermelon", "Pineapple", "Apricot", "3Maple"}
print(fruits) #everytime the position of item changes

#unchangeable ===> Mean you cannot change items in a set, you only add or remove items
#Duplicates Not Allowed ==> no two same items are allowed in a set