n,b=map(int,input().split())
data=list(map(int,input().split()))
data.sort()
num=data[:n]
res=(max(num)-min(num))
for i in range(1,len(data)-n+1):
    tem=data[i:i+n]
    add=(max(tem)-min(tem))
    if(res>add):
        res=add
print(res)