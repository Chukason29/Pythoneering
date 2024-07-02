if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
    scoreList = [i[1] for i in records].sort()
    print(scoreList)
        