import math
a=int(input())
for i in range(a):
    b=int(input())
    i=1
    out=0
    res=[]
    while(i<b):
        sum1=math.gcd(i,b)+i
        out=max(out,sum1)
        res.append(i)
        i+=1
    for i in res:
        if((math.gcd(i,b)+i)==out):
            print(i)
            break
        
        
    