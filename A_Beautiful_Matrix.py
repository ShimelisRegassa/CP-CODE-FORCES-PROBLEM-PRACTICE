matrix=[]
for i in range(5):
    row=list(map(int,input().split()))
    matrix.append(row)
distance=0
for i in range(5):
    for j in range(5):
        if(matrix[i][j]==1):
            distance=abs(i-2)+abs(j-2)
            break
print(distance)