"""
Lambda functions are short functions stored to a variable

They are only used once and can
"""

#Lets write a lambda function for adding two numbers

add = lambda x, y: x + y

print(add(3, 5)) #print 8

# string revrsal using recursion

def string_reverse(s):
    #base case
    if len(s) == 0:
        return s
    else:
        return s[-1] + string_reverse(s[:-1])

print(string_reverse("Grace"))