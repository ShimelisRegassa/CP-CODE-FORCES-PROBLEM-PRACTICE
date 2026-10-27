num=list(map(int,input().split()))
left=0
right=0
last=len(num)-1
while(right<=last):
    if(num[right]==0):
        num[left],num[right]=num[right],num[left]
        left+=1
        right+=1
    elif(num[right]==1):
        right+=1
    else:
        num[right],num[last]=num[last],num[right]
        last-=1
print(*num)
    