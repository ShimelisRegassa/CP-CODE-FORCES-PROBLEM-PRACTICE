l=int(input())
nums=list(map(int,input().split()))
k=int(input())
counter=0
for i in range(l):
    left=i
    add=0
    b=k
    while(left<l):
        if(nums[left]==1):
            left+=1
            add+=1
        else:
            if(b>0):
                left+=1
                add+=1
                b-=1
            else:
                break
    counter=max(counter,add)
print(counter)
    
            
                
            
    