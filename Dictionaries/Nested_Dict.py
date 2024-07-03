"""
Nested dict simply means a dict within a dict
"""
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#Accessing an item with a dict
print(myfamily["child1"]["name"]) #will print emil

#looping through a nested dict

for x in myfamily:
    print(f"\n{x}")
    for i, j in myfamily[x].items():
        print(f"\t{i}==>{j}")