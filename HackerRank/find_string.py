# length of subtring is  =  1; do a normal looping
#if s[i:] is equal to the length of substring , end the loop

def count_substring(string, sub_string):
    sub_string_length = len(sub_string)
    count = 0
    if sub_string_length == 1:
        for i in range(0, len(string)):
            if sub_string == string[i]:
                count = count + 1
    
    else:
        for i in range(0, len(string)):
            if len(string[i:]) == sub_string_length:
                if string[i: ] == sub_string:
                    count = count + 1
                    break
            else:
                word =  string[i : i + sub_string_length]
                if word == sub_string:
                   count = count + 1
    return count
    
                

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
    