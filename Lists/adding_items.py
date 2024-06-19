"""
Items can be added to a list
"""

NorthernStates = ["Adamawa", "Bauchi", "Kogi", "Zamfara", "Borno"]
SouthernStates = ["Abia", "Bayelsa", "Ondo", "Imo", "Rivers"]

#Appending item usingn append()
NorthernStates.append("Sokoto") #adding sokoto
print( NorthernStates)

SouthernStates.append("Ekiti") #adding Ekiti
print(SouthernStates)


#Inserting an item into a particular position
NorthernStates.insert(2, "Plateau")
print(NorthernStates)

SouthernStates.insert(4, "Edo")
print(SouthernStates)

# You can join other iterables likes a list, tuple, set, dict to a list using the extend()
SouthernStates.extend(NorthernStates)
print(SouthernStates)

NorthernStates.extend(SouthernStates)
print(NorthernStates)

#extending a list to a tuple or dict
NorthernStates.extend({"kebbi":"Kebbi", "taraba":"Taraba", "Gombe":"Gombe"})
print(NorthernStates)
