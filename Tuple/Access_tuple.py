"""
Tuples are like listxs just that you can mutate a tuple after declaration
Tuples are ordered==> Meaning they indexed the position of each item doesn't change with time we
Tuples are immutable ==> We cannnot add or remove item from a declared tuple
Tuples are used to store data that shouldn't be changed at all

"""
fruits = ("Apple", "Mango", "Orange", "Apricot", "Guavas", "Cherry", "Watermelon", "Pineapple", "Apricot", "3Maple")

#get first item
print(fruits[0])

#get last item
print(fruits[-1])

#Getting a range of items from a tuple
print(fruits[4:8]) #Getting guava to pineapple

#Getting a range using negative indexing
print(fruits[-5:-1])#Cherry to Apricot

#checkin if an item exits in a tuple
fruitCategory = "Avocado"
if fruitCategory in fruits:
    print(f"{fruitCategory} is found")
else:
    print(f"{fruitCategory} not found")

