"""
There are two main identity operators
"is" and "is not"
"""

x = ["benz", "toyota", "bmw"]
y = ["benz", "toyota", "bmw"]
z = x

#this prints  NOT OK because even if x and y have same items, they're not same objects
if( x is y):
    print("OK")
else:
    print("NOT OK")


#this prints "OK" because  x is equated to z
if( x is z):
    print("OK")
else:
    print("NOT OK")