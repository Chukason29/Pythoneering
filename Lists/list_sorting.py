"""
Sorting
"""
import random
fruits = ["Apple", "Mango", "Orange", "Apricot", "Guavas", "Cherry", "Watermelon", "Pineapple", "Apricot", "3Maple"]

#.sort() is used to sort alphanumerically in ascending order
fruits.sort()
print(fruits) #notice how 3Maple comes first

#from a random range of random numbers, bring out the highest figure

"""
*get the list of random number from 1-100
"""
randomNumbers = [random.randrange(1,101) for i in range(20)]
randomNumbers.sort()
print(randomNumbers)
maxNum = randomNumbers[-1]
print(maxNum)









