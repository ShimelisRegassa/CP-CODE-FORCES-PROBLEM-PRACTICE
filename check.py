k=int(input())
nums=list(map(int,input().split()))
long=float("inf")
current=0
left=0
for i in range(len(nums)):
    current+=nums[i]
    while(current>=k):
        long=min(long,i-left+1)
        current-=nums[left]
        left+=1
print(long)