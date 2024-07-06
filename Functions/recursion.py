"""
Recursion always starts from the end to handle the answer
"""
#Factorial
def factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))


# Fibonaccci Series
def fibonnacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0    
    else:
        return fibonnacci(n-1) +fibonnacci(n-2)
print(fibonnacci(6))



# Sum of all numbers in the list
def sumList (numList):
    if len(numList) == 0: #checks if the list is empty
        return 0
    else: # If list is not empty then
        return numList[0] + sumList(numList[1:]) #Add the first number to the remaining numbers
print(sumList([1, 2, 3, 4, 5]))

def reverse_string(theString):
    if len(theString) == 0:
        return theString
    else:
        return theString[-1] + reverse_string(theString[:-1])

print(reverse_string("Arsenal"))