from collections import Counter
k=int(input())
nums=list(map(int,input().split()))
val=nums[:k]
curr=sum(val)
res=0
check=Counter(val)
if(len(check)==k):
    res=curr
for i in range(k,len(nums)):
    curr-=nums[i-k]
    curr+=nums[i]
    check[nums[i]]+=1
    check[nums[i-k]]-=1
    if(check[nums[i-k]]==0):
         del check[nums[i-k]]
    if(len(check)==k):
        res=max(res,curr)
print(res)
        