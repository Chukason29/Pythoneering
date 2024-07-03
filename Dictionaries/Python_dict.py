'''
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
A dict. is just like a javascript object

dicts are accessed via their keys like JS objects
dicts do not allow duplicates
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#values of each key can be changed
thisdict["brand"] = "Mercedes"

print(thisdict)