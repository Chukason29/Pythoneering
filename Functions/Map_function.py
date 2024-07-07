"""
The map function is used to carry out an operation on every item on the list
"""
#Square of Numbers: Given a list of integers, return a list where each integer is squared.

squared = lambda n : n**2
myList = [2, 4, 6, 8, 1, 12]
squaredList = list(map(squared, myList))
print(squaredList)


#Convert Temperatures: Given a list of temperatures in Celsius, convert each temperature to Fahrenheit.
celciusToFahren = lambda n: (n * (9/5)) + 32
celciusList = [0, 37, 100]
tempList = list(map(celciusToFahren, celciusList))
print(tempList)