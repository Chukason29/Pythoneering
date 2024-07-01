"""
Like List, Tuples can be looped through using for in, for or while loops
"""
Continents = ("Africa", "Europe", "Asia", "South America", "North America", "Oceania", "Antartica")

search = "e"
for i in Continents:
    if "e" in i:
        print(f"{i}, contains {search}")
    else:
        print(f"{i}, does not conatin {search}")