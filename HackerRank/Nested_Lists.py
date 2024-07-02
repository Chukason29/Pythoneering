if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        records.sort()    
    
    scoreList = [i[1] for i in records]
    scoreList = set(scoreList)
    scoreList = list(scoreList)
    scoreList.sort()
    if len(scoreList) > 1:
        secondLowestScore = scoreList[1]
    else:
        secondLowestScore = scoreList[0]

    for i in records:
        if secondLowestScore in i:
            print(i[0])
        