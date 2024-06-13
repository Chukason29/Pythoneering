name1 = "Chukwuebuka Alaegbu"
#In python like most languages, strings are arrays of characters. 
#They can be looped through, modified, etc


#Looping through a string
name2 = "Yartomizan"
for i in name2:
    print(i)

#to get length of string, use len()
print(len(name2))

#to check for a substring within a string use the in keyword
if 'tomi' in name2:
    print("Yes, tomi is in", name2)

if "zzan" not in name2:
    print("Yes 'zzan' is not found in ", name2)

