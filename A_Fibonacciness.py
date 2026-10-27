t=int(input())
for i in range(t):
    data=list(map(int,input().split()))
    num=data[0]+data[1]
    data.insert(2,num)
    counter=0
    for i in range(2,len(data)):
        if(data[i]==data[i-1]+data[i-2]):
            counter+=1
    print(counter)