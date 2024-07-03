"""
Items can be added into a dict
"""
student = {
    "name" : "Victor",
    "age" : 26,
    "is_nigerian" : False,
    "othernames" : ["ebuka", "James", "Kelly"]
}

student["height"] = 1.65

print(student)


#.update() also adds items to a dict

student.update({"class": "JSS 2"})
print(student)