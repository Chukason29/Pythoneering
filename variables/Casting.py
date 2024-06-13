"""
Casting is a method of forcing a particular data type on a variable
"""

a = '5'

print(type(int(a))) # a is normally a string but because we casted it to an integer this will print out a string
print(int(a) + 7) # will give you 12

x = str(3)
y = int(3)
z = float(3)

print(f"{x}, {y}, {z}")