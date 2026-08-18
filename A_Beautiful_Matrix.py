data=[]
for i in range(5):
    row=[]
    row=list(map(int,input().split()))
    data.append(row)
distance=0
boolean=False
for i in range(5):
    for j in range(5):
        if(data[i][j]==1):
            distance=abs(2-i)+abs(2-j)
            boolean=True
    if(boolean) :
        break  
print(distance)       
        