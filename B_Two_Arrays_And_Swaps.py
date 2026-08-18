a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    data1=list(map(int,input().split()))
    data2=list(map(int,input().split()))
    data1.sort()
    data2.sort(reverse=True)
    for i in range(c):
        if(data2[i]>data1[i]):
            data1[i]=data2[i]
     
    print(sum(data1))
    