"""
dicts are accessed using keys
"""
student = {
    "name" : "Victor",
    "age" : 26,
    "is_nigerian" : False,
    "othernames" : ["ebuka", "James", "Kelly"]
}

print(student["name"])
# will gie you same result as 
print(student.get("name"))


#.keys() gives you all the keys of the dict in a list
dictKeys = student.keys()
print(dictKeys)

#.values() gives you all the values of the dict in a list
dictValues = student.values()
print(dictValues)