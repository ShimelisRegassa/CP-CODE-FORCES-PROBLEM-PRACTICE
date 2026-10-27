a=int(input())
for i in range(a):
    b=int(input())
    data=[0]*b
    for i in  range(b):
        c,d=map(int,input().split())
        if(c<=10):
             data[i]=d
    out=max(data)
    print(data.index(out)+1)
    