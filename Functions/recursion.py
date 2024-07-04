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