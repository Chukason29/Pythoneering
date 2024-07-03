"""
Looping through a dict
"""
student = {
    "name" : "Victor",
    "age" : 26,
    "is_nigerian" : False,
    "othernames" : ["ebuka", "James", "Kelly"]
}

#looping through the keys to get the value
for x in student:
    print(student[x])
