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