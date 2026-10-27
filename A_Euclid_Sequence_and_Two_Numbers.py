a=int(input())
for i in range(a):
    b=int(input())
    data=list(map(int,input().split()))
    data.sort(reverse=True)
    count=0
    for i in range(len(data)-2):
        if(data[i]%data[i+1]!=data[i+2]):
            print(-1)
            break
        else:
            count+=1
    if(count==b-2):
        print(data[0],data[1])