a=int(input())
for i in range(a):
    b,c,d=map(int,input().split())
    data=list(map(int,input().split()))
    v=sum(data)
    if(v==c):
        print("YES")
    elif(v>c):
        print("NO")
    else:
        di=c-v
        if(di%d==0):
            print("YES")
        else:
            print("NO")
    