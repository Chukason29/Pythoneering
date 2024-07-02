if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])    
    scoreList = [i[1] for i in records]
    scoreList.sort()
    secondLowestScore = scoreList[1]

    for i in records:
        if secondLowestScore in i:
            print(i[0])
        