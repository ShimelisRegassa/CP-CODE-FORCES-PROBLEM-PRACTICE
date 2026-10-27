t=int(input())
for i in range(t):
    n,k,x=map(int,input().split())
    g=0
    for i in range(1,k+1):
        if(i!=x):
            g=i
            break
    else:
        print("NO")
    if(g):
        if(n//g>=k and n-(g*(k-1))>0 and n-(g*(k-1))!=x):
            print("YES")
            for i in range(n//g):
                print(g, end=" " if i!=n//g-1 else "\n")
        else:
            print("NO")
        
        
            