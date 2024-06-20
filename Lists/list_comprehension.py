"""
list comprehension is execution of expression within a list construct
"""
import math
fruits = ["Apple", "Mango", "Orange", "Apricot", "Guavas", "Cherry", "Watermelon", "Pineapple", "Apricot"]

#return every item with letter "o"
Ofruits = [x for x in fruits if "o" in x]
print(Ofruits)

#return the square of all even numbers from 1-100
def evenSquares(n):
    return [i*i for i in range(n) if i%2 == 0]

print(evenSquares(10))