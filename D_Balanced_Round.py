t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    num=list(map(int,input().split()))
    num.sort()
    res=0
    l=0
    for i in range(1,a):
        if(num[i]-num[i-1]>b):
            l=i
        res=max(res,i-l+1)
    if(res!=0):
        print(a-res)
    else:
        print(0)