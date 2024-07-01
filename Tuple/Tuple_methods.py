"""
Let's See some methods of tuples
"""
Continents = ("Africa", "Europe", "Asia", "South America", "North America", "Oceania", "Antartica")
ContinentsList = ["Africa", "Europe", "Asia", "South America", "North America", "Oceania", "Antartica"]

#.count() tells you the number of items an item occurs in a tuple
print(Continents.count("Africa"))
print(Continents.count("Asia"))

#.index() tells you positioning of an item in a iterable
print(Continents.index("Africa")) #Prints zeros
