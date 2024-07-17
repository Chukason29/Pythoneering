"""
You are given a string S.
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
"""
if __name__ == '__main__':
    s = input()

    def alnum(n):
        verdict = "False"
        for i in n:
            if i.isalnum():
                verdict = "True"
                break
        return verdict
    
    def alpha(n):
        verdict = "False"
        for i in n:
            if i.isalpha():
                verdict = "True"
                break
        return verdict
    def numeric(n):
        verdict = "False"
        for i in n:
            if i.isdigit():
                verdict = "True"
                break
        return verdict

    def lower(n):
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
    
    print(alnum(s))
    print(alpha(s))
    print(numeric(s))
    print(lower(s))
    print(upper(s))