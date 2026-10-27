a=int(input())
for i in range(a):
    data=list(map(int,input().split()))
    a=set(data)
    if(len(a)==1):
        print("YES")
    else:
        print("NO")