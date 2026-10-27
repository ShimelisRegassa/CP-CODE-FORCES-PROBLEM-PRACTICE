a=int(input())
data=list(map(int,input().split()))
num=[0]*a
for i in data:
    num[i-1]=data.index(i)+1
print(*num)
    
