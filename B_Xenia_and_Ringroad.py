n,b=map(int,input().split())
num=list(map(int,input().split()))
total=num[0]-1
for j in range(1,len(num)):
    if(num[j]>=num[j-1]):
        total+=(num[j]-num[j-1])
    else:
        total+=((n-num[j-1]+1)+num[j]-1)
print(total)
