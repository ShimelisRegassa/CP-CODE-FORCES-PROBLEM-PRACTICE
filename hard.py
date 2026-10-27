from collections import Counter
nums=list(map(int,input().split()))
k=int(input())
right=0
left=0
counter1=0
counter2=0
count={}
lcount=Counter()
r=0
l=0
while(right<len(nums)):
    count[nums[right]]=count.get(nums[right],0)+1
    while(len(count)>k):
        count[nums[left]]-=1
        if(count[nums[left]]==0):
            del count[nums[left]]
        left+=1
    counter1+=(right-left+1)
    right+=1
while(r<len(nums)):
    lcount[nums[r]]+=1
    while(len(lcount)>k-1):
        lcount[nums[l]]-=1
        if(lcount[nums[l]]==0):
            del lcount[nums[l]]
        l+=1
    counter2+=(r-l+1)
    r+=1
if(k!=1):
    print (counter1-counter2)
else:
    print (counter1)