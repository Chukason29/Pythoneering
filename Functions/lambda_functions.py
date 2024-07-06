import math
"""
Lambda functions are short functions stored to a variable

They are only used once and can
"""

#Lets write a lambda function for adding two numbers
add = lambda x, y: x + y
print(add(3, 5)) #print 8


#Write a lambda function that takes two arguments, a and b, and returns their product. Use this lambda function to calculate the product of 4 and 5.
product = lambda a, b: a * b
print(product(4, 5))

#Given the list numbers = [1, 2, 3, 4, 5], use the map() function with a lambda to create a new list where each number is squared. Print the new list.
def square(n):
    return n**2

newList = lambda myList: list(map(square, myList))
print(newList([1, 2, 3, 4, 5]))


#Given the list ages = [5, 12, 17, 18, 24, 32], use the filter() function with a lambda to create a new list of ages greater than or equal to 18. Print the new list.
def ageGrade(n):
    if n >= 18:
        return n
newAges = lambda ageList: filter(ageGrade, ageList)

print(newAges([5, 12, 17, 18, 24, 32]))