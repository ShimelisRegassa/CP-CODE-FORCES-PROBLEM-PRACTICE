matrix=[list(map(int,input().split())) for i in range(5)]
row=len(matrix)
column=len(matrix[0])
sec=[[0]*row for _ in range(column)]
for i in range(row):
    for j in range(column):
        sec[j][i]=matrix[i][j]
for i in range(column):
    print(*sec[i])
    
         