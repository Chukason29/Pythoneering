"""
Sometimes you don't know how many arguments you
"""
#args return a tuple
def names (*args):
    print(args)

names("ebuka", "victor", "love", "jane")

#**kwargs are keyword arguments that can be 
# kwargs returns a dictionary
def humans(**kwargs):
    print (kwargs) 

humans(Male="orange", Female = "Mango")