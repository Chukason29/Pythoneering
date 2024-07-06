"""
Recursion always starts from the end to handle the answer
"""
#Factorial
def fact(n):
    if n > 1: #base case
        factorial = n * fact(n-1)
    else:
        factorial = 1
    return factorial

print(fact(5))

def factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

def fibonnacci(n):
    if n > 1:
        fibnum = fibonnacci(n-1) +fibonnacci(n + 1)
    else:
        n = 1
    return fibnum

