from sys import exit
def fun(arr):
    u=0
    v=1
    #u and v have been assigned so that input can be checked in cases such as (-1,-1,-1,X,X,X,O,O,O)
    #u and v are different for wrong outputs for(-1,-1,-1,O,O,O,X,X,X)
    for i in range(0,7,3):
        if arr[i]==arr[i+1] and arr[i+1]==arr[i+2]:
            if arr[i]=="X":
                u=1
            if arr[i]=="O":
                v=2
    if u==1:
        if x-o!=1:# this has to be true as X goes first
            print("INVALID INPUT",end='')
            exit(0)
        else:
            return 1
    elif v==2:
        if x-o!=0:# this has to be true as x goes first
            print("INVALID INPUT",end='')
            exit(0)
        else:
            return 2
    for i in range(0,3,1):
        if arr[i]==arr[i+3] and arr[i+3]==arr[i+6]:
            if arr[i]=="X":
                u=1
            if arr[i]=="O":
                v=2
    if u==1:
        if x-o!=1:
            print("INVALID INPUT",end='')
            exit(0)
        else:
            return 1
    elif v==2:
        if x-o!=0:
            print("INVALID INPUT",end='')
            exit(0)
        else:
            return 2
    if arr[0]==arr[4] and arr[4]==arr[8]:
        if arr[0]=="X":
            u=1
        if arr[0]=="O":
            v=2
    if u==1:
        if x-o!=1:
            print("INVALID INPUT",end='')
            exit(0)
        else:
            return 1
    elif v==2:
        if x-o!=0:
            print("INVALID INPUT",end='')
            exit(0)
        else:
            return 2
    if arr[2]==arr[4] and arr[4]==arr[6]:
        if arr[2]=="X":
            u=1
        if arr[2]=="O":
            v=2
    if u==1:
        if x-o!=1:
            print("INVALID INPUT",end='')
            exit(0)
        else:
            return 1
    elif v==2:
        if x-o!=0:
            print("INVALID INPUT",end='')
            exit(0)
        else:
            return 2
arr=[]
x=0
o=0
k=0
for i in range(9):#entering elements from user
    element = input()
    arr.append(element)
    if arr[i]!="X" and arr[i]!="O" and arr[i]!="-1":
        print("INVALID INPUT",end='')
        k=1
        break
    if arr[i]=="X":
        x+=1
    elif arr[i]=="O":
        o+=1
if k==1:
    exit(0)
if x!=o:
    print("INVALID INPUT",end='')
    exit(0)
if fun(arr)==1 or fun(arr)==2:
    print("INVALID INPUT",end='')
    exit(0)
count=0
list=[]
for j in range(9):
    if arr[j]=="-1":
        arr[j]="X"
        x+=1
        if fun(arr)==1:
            list.append([arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7],arr[8]])
        else:
            for l in range(9):
                if arr[l]=="-1":
                    arr[l]="O"
                    o+=1
                    if fun(arr)!=2:
                        for p in range(9):
                            if arr[p]=="-1":
                                arr[p]="X"
                                x+=1
                                if fun(arr)==1:
                                    list.append([arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7],arr[8]])
                                arr[p]="-1"
                                x-=1
                    arr[l]="-1"
                    o-=1
        arr[j]="-1"
        x-=1
sets=set()#converting into set as they store unique elements
for c in list:
    tuples=tuple(c)#converting into tuple as they are immutable and set can only store immutable objects
    sets.add(tuples)
count=len(sets)
print(count,end='')
