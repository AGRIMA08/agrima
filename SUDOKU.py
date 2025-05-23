from sys import exit
grid=[]
r=0
try:
    for i in range(9):
        row = list(map(int, input().split()))
        grid.append(row)
        if len(row)!=9:
            print("INVALID INPUT")
            exit(0)
except ValueError:
    print("INVALID INPUT")
#checking validity of input
for j in grid:
    for k in range(9):
        if j[k]<1 or j[k]>9:
            print("INVALID INPUT")
            exit(0)
for j in grid:
    #checking row element
    sets1=set()
    tuples=tuple(j)
    for i in range(9):
        sets1.add(tuples[i])
    if len(sets1)!=9:
        print("False",end='')
        exit(0)
for k in range(9):
    #checking column element
    column=[grid[l][k] for l in range(9)]
    sets2=set()
    tuples=tuple(column)
    for i in range(9):
        sets2.add(tuples[i])
    if len(sets2)!=9:
        print("False",end='')
        exit(0)
for i in range(0, 9, 3):
    #checking for grid
    for j in range(0, 9, 3):
        sets3 = set()
        for row in grid[i:i+3]:
            sets3.update(row[j:j+3])
        if len(sets3) != 9:
            print("False", end='')
            exit(0)
print("True",end='')
