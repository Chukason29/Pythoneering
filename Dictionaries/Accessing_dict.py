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

student["age"] = 45

print(student.values()) #value of age changed here

#.items() returns each key:pair as tuples in a list
for i in student.items():
    print(f"{i[0]} ==> {i[1]}")

##VERY IMPORTANT
#check if key exists  ==========>
if "age" in student:
    print("its found")
else:
    print("Not found")