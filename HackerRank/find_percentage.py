#Finding the percentage of a given student after entering the date of a specified number of students
if __name__ == '__main__':
    n = int(input()) # specifies the number of students
    student_marks = {} #create a dictionary to store the information provided
    for _ in range(n): #for the number records to be inputted
        
        # each input has a name and scores, .split() turns the input into a list then unpack. where the first item is name# and the remaing item is a list assigned to
        name, *line = input().split() 
        
        # for each of the items in line variables convert to float and store into scores
        scores = list(map(float, line))

        #each of the records, store into the dictionary
        student_marks[name] = scores

    #Choose the particular student you want to calculate the percentage   
    query_name = input()
    percetageNum = sum(student_marks[query_name])/ len((student_marks[query_name]))
    print(f"{round(percetageNum, 4):.2f}")