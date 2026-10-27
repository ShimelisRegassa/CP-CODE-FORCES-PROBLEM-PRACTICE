a=int(input())
for i in range(a):
    b=int(input())
    data=list(map(int,input().split()))
    data.sort()
    if(len(data)!=len(set(data))):
        print(0)
    else:
        count=max(data)
        for i in range(b-1):
            add=data[i+1]-data[i]
            count=min(count,add)
        print(count)