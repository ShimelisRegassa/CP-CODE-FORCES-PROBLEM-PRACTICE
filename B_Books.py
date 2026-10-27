n,t=map(int,input().split())
data=list(map(int,input().split()))
right=0
left=0
value=0
counter=0
while(right<len(data) ):
    value+=data[right]
    while(value>t and left<len(data)):
        value-=data[left]
        left+=1
    counter=max(counter,right-left+1)
    right+=1
print(counter)

    
    
        
        