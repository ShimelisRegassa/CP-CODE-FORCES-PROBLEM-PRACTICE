nums=list(map(int,input().split()))
num1=[0]*len(nums)
num2=[0]*len(nums)
for i in range(1,len(nums)):
    num1[i]=nums[i-1]+num1[i-1]
for j in range(len(nums)-2,-1,-1):
    num2[j]=nums[j+1]+num2[j+1]
res=[]
for i in range(len(nums)):
    c=(i*nums[i]-num1[i])+(num2[i]-(len(nums)-i-1)*nums[i])
    res.append(c)
print(res)