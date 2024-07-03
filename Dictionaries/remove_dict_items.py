"""
Removing dict items
"""
student = {
    "name" : "Victor",
    "age" : 26,
    "is_nigerian" : False,
    "othernames" : ["ebuka", "James", "Kelly"]
}

#.pop("itemName") remove the specified item
student.pop("age")
print(student)

#.popitem() removes the last item in a dict
student.popitem()
print(student)

#.clear() clears out all item in a dict
student.clear()

#del dict deletes the dict itself
del student