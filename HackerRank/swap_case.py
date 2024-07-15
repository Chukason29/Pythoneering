"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
"""

def swap_case(s):
    newWord = []
    for i in s:
        if i.isupper():
            newWord.append(i.lower())
        elif i.islower():
            newWord.append(i.upper())
    return ''.join(newWord)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)