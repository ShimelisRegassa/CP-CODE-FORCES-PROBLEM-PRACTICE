l=int(input())
nums=list(map(int,input().split()))
k=int(input())
val=0
left=0
counter=float("inf")
for i in range(len(nums)):
    val+=nums[i]
    while(val>=k):
        counter=min(counter,i-left+1)
        val-=nums[left]
        left+=1
if(counter==float("inf")):
    print(0)
else:
    print(counter)