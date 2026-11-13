t=int(input())
for  i in range(t):
    b=int(input())
    num=list(map(int,input().split()))
    for i in num:
        if(i%67==0):
            print("YES")
            break
    else:
        print("NO")