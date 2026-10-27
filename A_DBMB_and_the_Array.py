a=int(input())
for i in range(a):
    b,c,d=map(int,input().split())
    data=list(map(int,input().split()))
    num=sum(data)
    if(num>c):
        print("NO")
    else:
        num=c-num
        if(num%d==0):
            print("YES")
        else:
            print("NO")