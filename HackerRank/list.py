if __name__ == '__main__':
    n = int(input())
    myList = []
    for _ in range(n):
        entry = input()
        data = entry.split()
        if(data[0] == "insert"):
            myList.insert(int(data[1]), int(data[2]))
        elif(data[0] == "print"):
            print(myList)
        elif (data[0] == "remove"):
            myList.remove(int(data[1]))
        elif (data[0] == "append"):
            myList.append(int(data[1]))
        elif (data[0] == "sort"):
            myList.sort()
        elif (data[0] == "pop"):
            myList.pop()
        elif (data[0] == "reverse"):
            myList.reverse()
print(myList)