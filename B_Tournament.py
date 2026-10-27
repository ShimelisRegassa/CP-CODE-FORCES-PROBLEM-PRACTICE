t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    num=list(map(int,input().split()))
    val=num[b-1]
    val2=max(num)
    if(c>=2):
        print("YES")
    else:
        if(val==val2):
            print("YES")
        else:
            print("NO")
    