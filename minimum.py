l=int(input())
nums=list(map(int,input().split()))
k=int(input())
counter=l
val=0
right=0
left=0
while(left<l and right<l):
    val+=nums[left]
    if(val<k):
        left+=1
    elif(val>k):
        while(val>k):
            counter=min(counter,left-right+1)
            val-=nums[right]
            right+=1
        if(val==k):
            counter=min(counter,left-right+1)
            val-=nums[right]
            right+=1
            left+=1      
        else:
            left+=1
    else:
        counter=min(counter,left-right+1)
        val-=nums[right]
        left+=1
        right+=1
        
print(counter)
                
