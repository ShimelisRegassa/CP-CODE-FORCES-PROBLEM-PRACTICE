a=int(input())
for i in range(a):
    b=int(input())
    data=list(map(int,input().split()))
    num=set(data)
    if(len(data)==len(num)):
        print("YES")
    else:
        print("NO")