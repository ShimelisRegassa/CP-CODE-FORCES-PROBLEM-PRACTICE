n,t=map(int,input().split())
data=list(map(int,input().split()))
index=0
left=0
right=t
value=sum(data[:t])
current=value
while(right<len(data) and left<len(data)-t+1):
    current+=data[right]
    current-=data[left]
    right+=1
    left+=1
    if(current<value):
        index=left
        value=current
print(index+1)
    
    
    

