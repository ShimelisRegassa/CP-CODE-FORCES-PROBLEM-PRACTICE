num=list(map(int,input().split()))
t=int(input())
ob={0:-1}
val=0
current=float("inf")
res=float("inf")
check=[float("inf")]*len(num)
for j in range(len(num)):
    val+=num[j]
    if(val -t in ob):
        length=j-ob[val-t]
        start=ob[val-t]
        if(start>=0 and check[start]!=float("inf")):
            res=min(res,check[start]+length)
        current=min(current,length)
    check[j]=current
    ob[val]=j
print(res)
            
    
    