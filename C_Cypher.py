t=int(input())
for i in range(t):
    b=int(input())
    data=list(map(int,input().split()))
    res=[]
    for i in range(b):
        data1=input().split()
        move=data1[1]
        for m in move :
            if(m=="D"):
                data[i]=(data[i]+1)%10
            else:
                data[i]=(data[i]+9)%10
        res.append(data[i])
    print(*res)