#Using while loop to construct a multiplication table

x = int(input())
y = int(input())

count =  1

while count <= y:
    print(f"{x} x {count} ==> {x * count}")
    count = count + 1