"""
Unpacking tuples is needed is a concept where tuple items are assigned to variales
"""
Continents = ("Africa", "Europe", "Asia", "South America", "North America", "Oceania", "Antartica")

#let's unpack the tuples above 

(Nigeria, Germany, China, Brazil, Mexico, Australia, SnowLine) = Continents

print(Nigeria) # will print Africa
print(Germany) #will print Europe
print(China) #will print Asia

#Using astericks when unpacking
(Ghana, Englang, *theRest) = Continents

print(theRest)# This will print a list of the remaining items in the tuple aside the first two unpacked
