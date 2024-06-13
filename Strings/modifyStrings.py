name = "chukwuebuka"
text = " Grace Alaegbu "
name2 = "Chukwuebuka Victor Alaegbu"

#to uppercase
print(name.upper())

#to lowercase
print(name.lower())

#use the strip() method to remove white space at the beginning and end of a string
print(len(text)) # length is 15
print(len(text.strip())) #length is 13 cos the two white spaces at the end has been 

#replace() method replace a string with another string
print(text.strip().replace("Grace", "Polycarp")) #here the white space has been stripped and grace replaced with polycarp

#To split a given string using an instance
#let's split the string variable name2 using spaces as the separator

print(name2.split(" "))# This returns a list of the splited string
print(name.split("")) # this will throw an error because no separator was defined
