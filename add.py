k=int(input())
data=list(map(int,input().split()))
right=0
left=0
counter=0
val=0
while(right<len(data)):
    if(data[right]==0):
        val+=1
    while(val>k):
        if(data[left]==0):
            val-=1
        left+=1
    counter=max(counter,right -left+1)
    right+=1
print(counter)
    
