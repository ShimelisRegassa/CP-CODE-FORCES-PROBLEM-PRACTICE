a=int(input())
nums=list(map(int,input().split()))
right=0
left=0
for i in range(len(nums)-1):
    if(nums[i]>nums[i+1]):
        left=i
        break
for i in range(len(nums)-1,0,-1):
    if(nums[i]<nums[i-1]):
        right=i
        break
fir=nums[left:right+1]
fir.reverse()
res=nums[:left]+fir+nums[right+1:]
nums.sort()
if(nums==res):
    print("yes")
    print(left+1,right+1)
else:
    print("no")
