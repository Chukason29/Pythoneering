"""
Although we said before that we cannot mutate a tuple.
To do so, you must first convert to a list, then to mutate an reconvert to  TUPLE
"""

fruits = ("Apple", "Mango", "Orange", "Apricot", "Guavas", "Cherry", "Watermelon", "Pineapple", "Apricot", "3Maple")

#Let's remove first and last item from the tuple above
fruitsList = list(fruits)
fruitsList.remove(fruitsList[0])
fruitsList.remove(fruitsList[-1])

fruitsList.append("Avocado")

fruitsList = tuple(fruitsList)

print(fruitsList)