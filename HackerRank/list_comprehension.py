"""
Let's learn about list comprehensions! You are given three integers  
and  representing the dimensions of a cuboid along with an integer . 
Print a list of all possible coordinates given by  on a 3D grid where the sum of  
is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.

All permutations of  are:

Print an array of the elements that do not sum to .
"""

newRange = [ i for i in range(1,100)  if i%2 ==0]

#x = int(input())
#y = int(input())
#z = int(input())
#n = int(input())*/
x = 1
y = 1
z = 2
n = 3

outerList = []

for i in range(x + 1):
    for j in range(y+1):
        for k in range(z + 1):
            outerList.append([i,j,k])
print(outerList)

#Instead of using the above, why not try using List Comprehension Below

permutations = [[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1)]
print(permutations)
total = [i for i in permutations if sum(i) != n]
print(total)