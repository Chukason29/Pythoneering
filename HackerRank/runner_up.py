if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scoreArr = list(arr) #converting a map to a list
    scoreArr = set(scoreArr) #removing duplicate
    scoreArr = list(scoreArr) #making it a list again
    scoreArr.sort()
    print(scoreArr)
