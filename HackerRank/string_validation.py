"""
You are given a string S.
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
"""
if __name__ == '__main__':
    s = input()
    if s.isalnum():
        print("True")
    else:
        print("False")
    if s.isalpha():
        print("True")
    else:
        print("False")
    if s.isnumeric():
        print("True")
    else:
        print("False")
    if s.islower():
        print("True")
    else:
        print("False")
    if s.isupper():
        print("True")
    else:
        print("False")