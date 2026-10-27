import math
a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    num=list(map(int,input().split()))
    sma=min(num)
    ind=num.index(sma)
    long=1
    left=ind+1
    while(left<b):
        if(sma+1==num[left]):
            sma=num[left]
            long+=1
        left+=1
    res=b-long
    res=res/c
    res=math.ceil(res)
    print(res)
            