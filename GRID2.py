def calculate(mat):
    if not mat:
        return 0,(-1, -1)
    n=len(mat)
    m=len(mat[0])
    A=[[0]*m for _ in range(n)] #defining a matrix to store the size
    maximum=0
    coordinate = (-1, -1)
    for i in range(n):
        for j in range(m):
            if mat[i][j]==1:
                if i==0 or j == 0:
                    A[i][j]= 1#because it will be one cell
                else:
                    A[i][j]=min(A[i-1][j], A[i][j-1], A[i-1][j-1])+1#the size of the square ending at(i,j)depends on the minimum size of the squares that end previously and then adding 1 for this cell
                if A[i][j]>maximum:
                    maximum=A[i][j]
                    coordinate=(i-maximum+1,j-maximum+1)
    return maximum,coordinate
n, m=map(int, input().split())
mat=[]
for i in range(n):
    row=list(map(int, input().split()))
    mat.append(row)
size,coordinate=calculate(mat)
print(size)
print(coordinate[0],coordinate[1])
