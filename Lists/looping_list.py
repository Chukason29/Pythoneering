"""
Looping through the list
"""
fruits = ["Apple", "Mango", "Orange", "Apricot", "Guavas", "Cherry", "Watermelon", "Pineapple", "Apricot"]

#thru for in loop
for i in fruits:
    print(i)
print("#######################################################")
#thru index number
for i in range(len(fruits)):
    print(fruits[i])
print("#######################################################")
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i+1
print("#######################################################")

#Looping thru list comprehension
#syntax ===> [expression ite]

newFruits = [print(x) for x in fruits]