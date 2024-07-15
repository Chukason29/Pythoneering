if __name__ == '__main__':
    n = int(input())
    myList = []
    for _ in range(n):
        entry = input()
        data = entry.split()
        if(data[0] == "insert"):
            myList.insert(data[1], data[2])
        elif(data[0] == "print"):
            print(myList)
        elif (data[0] == "remove"):
            myList.remove(data[1])
        elif (data[0] == "append"):
            myList.append(data[1])
        elif (data[0] == "sort"):
            myList.sort()
        elif (data[0] == "pop"):
            myList.pop()
        elif (data[0] == "reverse"):
            myList.reverse()
    
print(data)