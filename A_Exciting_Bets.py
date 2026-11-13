t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if(a==b):
        print(0,0)
    else:
        d=a%(abs(a-b))
        print(abs(a-b),min(d,abs(a-b)-d))