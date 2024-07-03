"""
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) 
of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
"""

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
        