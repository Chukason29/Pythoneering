set1 = {'a', 'b','c'}
set2 = {'x', 'y', 'z', 'b'}

#.union() and  '|' join sets together

set3 = set1.union(set2)
print(set3)
###### OR  ##########
set4 = set1 | set2
print(set4)


#.intersection() returns just the items in all the sets involved
print(set1.intersection(set2)) #return 'b' cos it is the common item

set1.intersection_update(set2) #returns the common item and changes the set the method is working upon
print(set1)

# .difference() is used to get the items that aren't common to both sets
print(set3.difference(set2))


#LEARN ALL THESE BELOW
#.difference_update()
#.symmetric_difference()
#.symmetric_difference_update()