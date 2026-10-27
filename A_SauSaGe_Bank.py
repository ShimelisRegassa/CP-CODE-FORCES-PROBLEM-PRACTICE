t=int(input())
for u in range(t):
    n,x=map(int,input().split())
    if(n==x):
        print(2*n)
    else:
        d=n-x
        print(2**(d+1)+(2*(x-1)))