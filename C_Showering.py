t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    maxprevoius=0
    boolean=False
    for i in range(a):
        m,n=map(int,input().split())
        diff=m-maxprevoius
        maxprevoius=max(maxprevoius,n)
        if(diff>=b):
            boolean=True
    if(c-maxprevoius>=b):
        boolean=True
    if(boolean):
        print("YES")
    else:
        print("NO")
    print("_".isdigit())