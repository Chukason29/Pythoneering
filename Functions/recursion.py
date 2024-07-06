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

