"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
"""
import re #used for regular expressions
def swap_case(s):
    newWord = []
    for i in s:
        x = re.findall("[a-zA-Z]", i) #checking if a letter is special character
        if x:
            if i.isupper():
                newWord.append(i.lower()) #change to lower
            elif i.islower():
                newWord.append(i.upper()) #change to upper
        else:
            newWord.append(i)
    return "".join(newWord)# joined all list items to a single word

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)