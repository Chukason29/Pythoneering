"""
List looks more like arrays in javascript
"""

friends = ["Wisdom", "Tommyzan", "Udo", "Great", "Mordecai"]
num = 2

print(friends[2]) #prints udo

#negative indexing
print(friends[-3]) #prints Udo
print(friends[-1]) #prints Mordecai


#slicing lists
print(friends[2:4]) #prints udo and great

print(friends[2:])#prints from Udo to the end
print(friends[:3])#prints from start to Udo


#check if item exist in a list

if "Great" in friends:
    print("YES")
else:
    print("NO")

if "Ebuka" not in friends:
    print("ebuka is not there")
else:
    print("ebuka is there")