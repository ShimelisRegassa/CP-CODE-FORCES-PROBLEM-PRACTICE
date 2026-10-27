t=int(input())
for i in range(t):
    b=int(input())
    num=list(map(int,input().split()))
    num.sort()
    data1=[]
    data2=[]
    for i in range(len(num)):
        if(i<b):
            data1.append(num[i])
        else:
            data2.append(num[i])
    dis=0
    for i in range(b-1):
        dis+=(data1[i+1]-data1[i])
        dis+=(data2[i+1]-data2[i])
    print(dis)
    for i in range(b):
        print(data1[i],data2[i])
        