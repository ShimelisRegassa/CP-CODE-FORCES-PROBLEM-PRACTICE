t=int(input())
for i in range(t):
    b=int(input())
    data=list(map(int,input().split()))
    val1=max(data)
    val2=min(data)
    fir=data.index(val1)
    sec=data.index(val2)
    data[fir]=data[0]
    data[sec]=data[1]
    data[0]=val1
    data[1]=val2
    if(data[1]!=data[0]):
        print("YES")
        print(*data)
    else:
        print("NO")
                