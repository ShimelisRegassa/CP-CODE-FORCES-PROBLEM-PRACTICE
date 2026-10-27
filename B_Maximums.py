n=int(input())
num=list(map(int,input().split()))
res=[0]*n
res[0]=num[0]
maximum=res[0]
for j in range(1,n):
    if(maximum<res[j-1]):
        maximum=res[j-1]
    res[j]=num[j]+maximum
print(*res)