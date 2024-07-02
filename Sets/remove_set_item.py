fruits = {"Apple", "Mango", "Orange", "Apricot", "Guavas", "Cherry", "Watermelon", "Pineapple", "Apricot", "3Maple"}
#.remove() or .discard() remove a particular item from the set
fruits.remove("Mango")
fruits.discard("Apple")
print(fruits)

#.pop() is used to remove random item from the list

fruits.pop()
print(fruits)

#.clear() removes all the items in the set
fruits.clear()
print(fruits)

#del delete the set itself
del fruits
print(fruits)# will give an error cos the set o longer exists