import math
a=int(input())
for i in range(a):
    b,c,d=map(int,input().split())
    if(b<c):
        num=c-b
        out=num/(2*d)
        print(math.ceil(out))
    else:
        num=b-c
        out=num/(2*d)
        print(math.ceil(out))
        
   