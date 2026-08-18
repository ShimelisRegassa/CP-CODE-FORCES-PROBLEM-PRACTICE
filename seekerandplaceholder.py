a=int(input())
data=list(map(int,input().split()))
left=0
right=0
for i in range(len(data)):
    if(data[i]==0):
        left=i
        right=i
        break
while(right<len(data)):
    if(data[right]!=0):
        data[left],data[right]=data[right],data[left]
        left+=1
    else:
        right+=1
print(*data)