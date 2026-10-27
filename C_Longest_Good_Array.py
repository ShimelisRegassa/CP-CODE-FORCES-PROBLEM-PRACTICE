import math
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    difference=b-a
    difference*=2
    dec=1+4*difference
    dec=math.sqrt(dec)
    dec=(dec-1)//2
    dec=int(dec)
    print(dec+1)
    