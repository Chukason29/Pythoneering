"""
You are given a string S.
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
"""
if __name__ == '__main__':
    #s = input()
    #for x in s:
        #if not x.
    def alnum(x):
        verdict = ""
        if x.isalnum():
            verdict = "True"
        else:
            x.verdict = "False"
        return verdict

    def alpha(n: str):
        verdict = "False"
        for i in n:
            if i.isalpha():
                verdict = "True"
                break
        return verdict
    def numeric(n):
        verdict = "False"
        for i in n:
            if i.isnumeric():
                verdict = "True"
                break
        return verdict

    def lower(n: str):
        verdict = "False"
        for i in n:
            if i.islower() and not i.isupper():
                verdict = "True"
                break
        return verdict
    def upper(n):
        verdict = "False"
        for i in n:
            if i.isupper():
                verdict = "True"
                break
        return verdict
    
    #print(alnum(s))
    #print(alpha(s))
    #print(numeric(s))
    print(not "A123#".isupper())
    #print(upper(s))