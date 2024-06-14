"""
Format string is needed for concatenating two different types without running into error
"""

age = 29
name = "Victor"

#print( age + name) ##returns error
print(f"{name} is {age} years") #doesn't return any error