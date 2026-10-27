a=int(input())
for i in range(a):
    data=list(map(int,input().split()))
    out=[]
    num=max(data)
    for i in data:
        if(i!=num):
            add=num-i
            out.append(add+1)
        else:
            if(data.count(num)==1):
                out.append(0)
            else:
                out.append(1)
    print(*out)
    