if __name__ == '__main__':
    n = int(input())
    inputs = tuple(map(int, input().split()))
    print(hash(inputs)) # printing out the hash tuple